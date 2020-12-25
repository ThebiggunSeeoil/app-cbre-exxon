from sys import modules
from django.db import models
from django.urls import reverse
import datetime
# date = datetime.datetime.now()
# print (date)
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255,unique=True) # กำหนด unique=True เพื่อป้องกันไม่ให้ใช้ชื่อที่ซ้ำกัน
    slug=models.SlugField(max_length=255,unique=True) # กำหนด เป็นการตั้งชื่อเล่นให้ข้อมูล หรือ กำหนดหมวดหมู่ หรือ Group ข้อมูล ทำให้เพิ่มความรวดเร็วในการเลือกข้อมูลแบบ Group

    def __str__(self):
        return self.name

    class Meta : 
        ordering = ('name',) # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'หมวดหมุ่สินค้า' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
        verbose_name_plural = 'ข้อมูลประเภทสินค้า' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
    
    def get_url(self):
        return reverse('product_by_category',args=[self.slug])


class Product(models.Model):
    name=models.CharField(max_length=255,unique=True) # กำหนด unique=True เพื่อป้องกันไม่ให้ใช้ชื่อที่ซ้ำกัน
    slug=models.SlugField(max_length=255,unique=True) # กำหนด เป็นการตั้งชื่อเล่นให้ข้อมูล หรือ กำหนดหมวดหมู่ หรือ Group ข้อมูล ทำให้เพิ่มความรวดเร็วในการเลือกข้อมูลแบบ Group
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE) # หากมีการลบช้อมูลที่มีการอ้างอิงหากัน ระบบจะทำการลบออกทั้งหมวดหมู๋
    image=models.ImageField(upload_to="product",blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta : 
        ordering = ('name',) # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'สินค้า' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
        verbose_name_plural = 'ข้อมูลสินค้า' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
    
    def get_url(self):
        return reverse('productDetail',args=[self.category.slug,self.slug])


class Cart(models.Model):
    cart_id=models.CharField(max_length=255,blank=True) # กำหนด blank=True กำหนดให้เป็นค่าว่างได้ หากยังไม่มีการใส่ข้อมูลเข้ามา
    date_added=models.DateTimeField(auto_now_add=True) # auto_now_add ให้ทำการระบุ Current date time 

    def __str__(self):
        return self.cart_id

    class Meta :
        db_table='cart'
        ordering=('date_added',)
        verbose_name = 'ตะกร้าสินค้า' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
        verbose_name_plural = 'ข้อมูลตระกร้าสินค้า' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta :
        db_table='cartItem'
        verbose_name = 'รายการสินค้าในตะกร้า' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
        verbose_name_plural = 'ข้อมูลรายการสินค้าในตะกร้า' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
    
    def sub_total (self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name

class Order (models.Model):
    name=models.CharField(max_length=255 , blank=True)
    address=models.CharField(max_length=255, blank=True)
    city=models.CharField(max_length=255, blank=True)
    postcode=models.CharField(max_length=255, blank=True)
    total=models.DecimalField(max_digits=10,decimal_places=2)
    email=models.EmailField(max_length=250,blank=True)
    token=models.CharField(max_length=255,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta :
        db_table='Order'
        ordering=('id',) # ทำการเรียงลำดับ ID จากน้อยไปหามาก เหมือน order by SQL

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product=models.CharField(max_length=250)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    order=models.ForeignKey(Order,on_delete=models.CASCADE) #ForeignKey คือ การใช้อ้างถึงตารางอื่น แบบเดียวกับการ Join sql  และ CASACDE คืือการทำให้เกิดการลบข้อมูลทั้งสองตารางหากมีการตารางไหนมีการสั่ง  Delete
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='OrderItem'
        ordering=('order',) # ทำการเรียงลำดับ ID จากน้อยไปหามาก เหมือน order by SQL

    def sub_total(self):
        return self.quantity*self.price

    def __str__(self):
        return self.product

class SiteList(models.Model):
    customer=models.CharField(max_length=255)
    pbl=models.CharField(max_length=255)
    internal_order=models.CharField(max_length=255)
    name=models.CharField(max_length=255,unique=False) # กำหนด unique=True เพื่อป้องกันไม่ให้ใช้ชื่อที่ซ้ำกัน
    regiter_name=models.CharField(max_length=255,unique=False) # กำหนด unique=True เพื่อป้องกันไม่ให้ใช้ชื่อที่ซ้ำกัน
    eng_name=models.CharField(max_length=255,unique=True) # กำหนด unique=True เพื่อป้องกันไม่ให้ใช้ชื่อที่ซ้ำกัน
    area=models.CharField(max_length=255,unique=False)
    tm=models.CharField(max_length=255)
    am=models.CharField(max_length=255)
    moso=models.CharField(max_length=255)
    moso_type=models.CharField(max_length=255)
    cat_type=models.CharField(max_length=255)
    # slug=models.SlugField(max_length=255,unique=True) # กำหนด เป็นการตั้งชื่อเล่นให้ข้อมูล หรือ กำหนดหมวดหมู่ หรือ Group ข้อมูล ทำให้เพิ่มความรวดเร็วในการเลือกข้อมูลแบบ Group
    # description=models.TextField(blank=True)
    # price=models.DecimalField(max_digits=10,decimal_places=2)
    # category=models.ForeignKey(Category,on_delete=models.CASCADE) # หากมีการลบช้อมูลที่มีการอ้างอิงหากัน ระบบจะทำการลบออกทั้งหมวดหมู๋
    # image=models.ImageField(upload_to="product",blank=True)
    # stock=models.IntegerField()
    # available=models.BooleanField(default=True)
    # created=models.DateTimeField(auto_now_add=True)
    # updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pbl

    class Meta : 
        ordering = ('name',) # ทำหน้าที่เรียงลำดับการแสดงผลที่หน้าเวบ
        verbose_name = 'สถานี' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
        verbose_name_plural = 'ข้อมูลสถานี' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
    
    # def get_url(self):
    #     return reverse('productDetail',args=[self.category.slug,self.slug])



class WahSubmit(models.Model):
    workorder=models.CharField(max_length=255)
    company=models.CharField(max_length=255)
    opended=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    startwork=models.CharField(max_length=255)
    completedwork=models.CharField(max_length=255)
    caller=models.CharField(max_length=255)
    wah_status=models.CharField(max_length=255)
    timestramp=models.DateTimeField(auto_now_add=True)
    planned_date=models.CharField(max_length=255 , blank=True)
    job_description=models.TextField(blank=True)
    fls_mame=models.CharField(max_length=255 ,blank=True)
    fls_phone=models.CharField(max_length=255, blank=True)
    management=models.CharField(max_length=255, blank=True)
    remark=models.TextField(blank=True)
    type_job=models.CharField(max_length=255,blank=True)
    jla_ra=models.CharField(max_length=255, blank=True)
    any_ssw=models.CharField(max_length=255, blank=True)
    physical=models.CharField(max_length=255,blank=True)
    fm=models.CharField(max_length=255,blank=True)
    

    class Meta :
        db_table='wah_submit'
        verbose_name = 'รายการ Submit WAH' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
        verbose_name_plural = 'รายละเอียดรายการ Submit WAH' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
    
    # def pending_total (self):
    #     return self.product.price * self.quantity

    def __str__(self):
        return self.workorder

class WahSubmitcontractor(models.Model):
    workorder=models.CharField(max_length=255)
    company=models.CharField(max_length=255)
    opended=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    startwork=models.CharField(max_length=255)
    completedwork=models.CharField(max_length=255)
    caller=models.CharField(max_length=255)
    wah_status=models.CharField(max_length=255)
    timestramp=models.DateTimeField(auto_now_add=True)
    planned_date=models.CharField(max_length=255 , blank=True)
    job_description=models.TextField(blank=True)
    fls_mame=models.CharField(max_length=255 ,blank=True)
    fls_phone=models.CharField(max_length=255, blank=True)
    management=models.CharField(max_length=255, blank=True)
    remark=models.TextField(blank=True)
    type_job=models.CharField(max_length=255,blank=True)
    jla_ra=models.CharField(max_length=255, blank=True)
    any_ssw=models.CharField(max_length=255, blank=True)
    physical=models.CharField(max_length=255,blank=True)
    fm=models.CharField(max_length=255,blank=True)
    

    class Meta :
        db_table='wah_submit_contractor'
        verbose_name = 'รายการ Submit WAH' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
        verbose_name_plural = 'รายละเอียดรายการ Submit WAH' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
    
    # def pending_total (self):
    #     return self.product.price * self.quantity

    def __str__(self):
        return self.workorder

class WahSubmitforcontractor(models.Model):
    workorder=models.CharField(max_length=255)
    company=models.CharField(max_length=255)
    company_id=models.IntegerField(blank=True,null=True)
    opended=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    startwork=models.DateTimeField(default=None,blank=True,null=True)
    completedwork=models.DateTimeField(default=None,blank=True,null=True)
    fls_startwork=models.CharField(max_length=255)
    fls_completedwork=models.CharField(max_length=255)
    caller=models.CharField(max_length=255)
    wah_status=models.CharField(max_length=255)
    timestramp=models.DateTimeField(auto_now_add=True)
    planned_date=models.DateField(default=None,blank=True,null=True)
    job_description=models.TextField(blank=True)
    fls_mame_1=models.CharField(max_length=255 ,blank=True)
    fls_mame_2=models.CharField(max_length=255 ,blank=True)
    fls_id_1=models.IntegerField()
    fls_id_2=models.IntegerField()
    fls_phone=models.CharField(max_length=255, blank=True)
    management=models.CharField(max_length=255, blank=True)
    remark=models.TextField(blank=True)
    type_job=models.CharField(max_length=255,blank=True)
    jla_ra=models.CharField(max_length=255, blank=True)
    any_ssw=models.CharField(max_length=255, blank=True)
    physical=models.CharField(max_length=255,blank=True)
    fm=models.CharField(max_length=255,blank=True)
    

    class Meta :
        db_table='wah_submit_for_contractor'
        verbose_name = 'รายการ Submit WAH' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
        verbose_name_plural = 'รายละเอียดรายการ Submit WAH' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
    
    # def pending_total (self):
    #     return self.product.price * self.quantity

    def __str__(self):
        return self.workorder
class WorkPending(models.Model):
    workorder=models.CharField(max_length=255)
    priority=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    opended=models.CharField(max_length=255)
    startwork=models.CharField(max_length=255)
    completedwork=models.CharField(max_length=255)
    caller=models.CharField(max_length=255)
    building_location=models.CharField(max_length=255)
    service_provider=models.CharField(max_length=255)
    equipment_code=models.CharField(max_length=255)
    failure_code=models.CharField(max_length=255,blank=True)
    problem_code=models.CharField(max_length=255)
    work_type=models.CharField(max_length=255)
    problum=models.TextField(blank=True)

    class Meta :
        db_table='WorkPending'
        verbose_name = 'งาน WAH SUBMIT' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
        verbose_name_plural = 'รายละเอียดงาน WAH SUBMIT' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
    
    # def pending_total (self):
    #     return self.product.price * self.quantity

    def __str__(self):
        return self.workorder

class Workfromgmail(models.Model):
    date_now = datetime.datetime.now()
    workorder=models.CharField(max_length=255,blank=True,null=True)
    opended=models.CharField(max_length=255,blank=True,null=True)
    caller=models.CharField(max_length=255,blank=True,null=True)
    service_provider=models.CharField(max_length=255,blank=True,null=True)
    service_id=models.IntegerField(blank=True,null=True)
    problum=models.TextField(blank=True,null=True)
    fm=models.TextField(blank=True,null=True)
    status_submit=models.CharField(max_length=255,blank=True,null=True)
    timestramp=models.DateTimeField(auto_now_add=True)
    time_create=models.CharField(max_length=255,blank=True,null=True)
    date=models.CharField(max_length=255,blank=True,null=True)
    notify_contractor=models.CharField(max_length=255,blank=True,null=True)
    completed_work=models.CharField(max_length=255,blank=True,null=True)
    
    
    class Meta :
        db_table='Workfromgmail'
        verbose_name = 'งาน work from gmail ' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
        verbose_name_plural = 'รายละเอียดงาน work from gmail' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
    
    # def pending_total (self):
    #     return self.product.price * self.quantity

    def __str__(self):
        return self.workorder

class Workfromgmail_new (models.Model):
    
    workorder=models.CharField(max_length=255,blank=True,null=True)
    opended=models.CharField(max_length=255,blank=True,null=True)
    caller=models.CharField(max_length=255,blank=True,null=True)
    service_provider=models.CharField(max_length=255,blank=True,null=True)
    service_id=models.IntegerField(blank=True,null=True)
    problum=models.TextField(blank=True,null=True)
    fm=models.TextField(blank=True,null=True)
    date_create=models.DateTimeField(auto_now_add=True)
    time_make=models.DateTimeField(auto_now_add=True)
    time_create=models.CharField(max_length=255,blank=True,null=True)
    
    
    class Meta :
        db_table='Workfromgmail_new'
        verbose_name = 'งาน work from gmail new ' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
        verbose_name_plural = 'รายละเอียดงาน work from gmail new' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
    
    # def pending_total (self):
    #     return self.product.price * self.quantity

    def __str__(self):
        return self.workorder







class PersanalDetaillogin (models.Model):
    name=models.CharField(max_length=200)
    user_type=models.CharField(max_length=200,blank=True,null=True)
    position=models.CharField(max_length=255,blank=True)
    company=models.CharField(max_length=255,blank=True)
    company_id=models.IntegerField(blank=True , null=True)
    key_login=models.TextField(max_length=6,blank=True,null=True) 
    line_id=models.TextField(max_length=255,blank=True, null=True)
    group_id=models.TextField(max_length=255,blank=True,null=True)
    richmenu_id=models.TextField(max_length=255,blank=True,null=True)
    member_status=models.CharField(max_length=255,blank=True,default='none')
    timestramp=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    class Meta :
        db_table='persanaldetaillogin'
        verbose_name = 'รายการพนักงาน' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
        verbose_name_plural = 'รายละเอียดพนักงาน' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
    
    # def pending_total (self):
    #     return self.product.price * self.quantity
    def __str__(self):
        return self.name

class type_of_work (models.Model):
    type_work=models.CharField(max_length=200,blank=True,null=True)
    type_detail=models.CharField(max_length=200,blank=True,null=True)
    
    
    class Meta :
        db_table='type_of_work'
        verbose_name = 'รายการทำงาน' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
        verbose_name_plural = 'รายละเอียดชนิดของงาน' # แปลงให้ข้อมูลหน้าเวบเป็นภาษาไทย 
    
    # def pending_total (self):
    #     return self.product.price * self.quantity
    def __str__(self):
        return self.type_detail



    
    



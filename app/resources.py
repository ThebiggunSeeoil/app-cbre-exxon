#resources.py
from import_export import resources
from app.models import SiteList , WorkPending
 
class SiteListResource(resources.ModelResource):
    class Meta:
        model = SiteList

class WorkPending_resource(resources.ModelResource):
    class Meta:
        model = WorkPending
        skip_unchanged = True
        report_skipped = False
        fields = ('workorder','completedwork')

    
        



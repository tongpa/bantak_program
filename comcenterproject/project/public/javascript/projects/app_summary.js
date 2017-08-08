Ext.application({
    name: 'projects',
    launch: function() {
    
        maintenance.listDivision.load();
        projects.listProjectType.load();
        projects.listSection.load();
        projects.listStatus.load();
        
        
        var listAllProject = new projects.ListProject({
        //	title:'แสดงรายการโครงการ',
        	renderTo : 'maintenance-app'
        	 
        	
        }); 
        /*
        var addProject = new projects.AddProject({
        	title : 'แบบฟอร์ม'
        }); 
          
         
        var project_main = new Ext.tab.Panel({
        	renderTo : 'maintenance-app',
        	items : [  listAllProject
        	]
        });
         */
    }
});
Ext.namespace("projects");
Ext.namespace("maintenance");
 
 
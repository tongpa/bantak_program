Ext.Loader.setConfig({enabled: true}); 

Ext.Loader.setPath('Ext.ux', '/javascript/extjs/examples/ux');
Ext.require([
             
             'Ext.form.*',
             'Ext.layout.container.Column',
             'Ext.ux.form.MultiSelect',
             'Ext.ux.form.ItemSelector',
             'Ext.tip.QuickTipManager',
             'Ext.ux.ajax.JsonSimlet',
             'Ext.ux.ajax.SimManager',             
             'Ext.window.MessageBox'
             
         ]);
 
 

Ext.application({
    name: 'coms',
    launch: function() {
    	Ext.tip.QuickTipManager.init();
    	
    	 
    	
    	var listRisk  = Ext.create('coms.view.AddCom', {
    		level : level, 
    		width : 900,
    		renderTo : 'maintenance-app',
    		title : 'รายการความเสียง'
    	}); 
    	
    	 
    	
    	 
    	listRisk.loadStore();
     
 
 
    	 
     
    	
    	//debugger;
    }
});
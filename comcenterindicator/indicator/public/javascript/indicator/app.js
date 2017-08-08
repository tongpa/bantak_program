Ext.Loader.setConfig({enabled: true});
//Ext.Loader.setPath('Ext.ux', '/ux');

Ext.Loader.setPath('Ext.ux', '/javascript/extjs/examples/ux');
Ext.Loader.setPath('risks', '/javascript/risk');
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
    name: 'indicator',
    launch: function() {
    	Ext.tip.QuickTipManager.init();
     
    	var indicator  = Ext.create('indicator.view.AddIndicator', {
    		level : level, 
    		width : 600,
    		title : 'รายงานตัวชี้วัด'
    	}); 
    	
    	var reportKPI  = new Ext.form.Panel({
 			title : 'รายงานตัวชี้วัด',
 			height : 520 ,
			items:[
				{
					html:"<br>&nbsp;&nbsp;1.<a href='/indicator/report1'  target='_blank'> ตัวชี้วัดตามหน่วยงาน</a>",
					xtype : "panel",
					border : false					
				},
				{
					html:"<br>&nbsp;&nbsp;2.<a href='/indicator/report2' target='_blank'> สรุปตัวชี้วัดประจำปี</a>",
					xtype : "panel",
					border : false					
				} 
			]
		});
   	
     
    	indicator.loadStore();
    	
    	Ext.create('Ext.tab.Panel',{
    		renderTo : 'maintenance-app',
    		items : [ indicator,reportKPI  ]
    	});
    	
     
    	
    	//debugger;
    }
});
 
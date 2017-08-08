Ext.Loader.setConfig({enabled: true});
//Ext.Loader.setPath('Ext.ux', '/ux');

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
    name: 'risks',
    launch: function() {
    	Ext.tip.QuickTipManager.init();
     
    	var ddd  = Ext.create('risks.view.AddRisk', {
    		width : 800,
    		//renderTo : 'maintenance-app',
    		title : 'รายงานอุบัติการณ์'
    	}); 
    	ddd.forAnonymousUser();
    	ddd.loadStore();
     
    	var listRiskinMonth  = Ext.create('risks.view.ListRiskInMonth', {    
    		width : 800 
    	}); 
    	listRiskinMonth.loadStore();
    	
    	Ext.create('Ext.Panel',{
    		border : false,			 
			autoWidth : true,
			anchor: '100%',
    		renderTo : 'maintenance-app',
    		items : [ ddd,listRiskinMonth ]
    	});
    	
    	
    	
    	//debugger;
    }
});
/*
Ext.onReady(function(){

    Ext.define('Employee', {
        extend: 'Ext.util.Observable',
        constructor: function(config){
            this.name = config.name;
            this.addEvents({
                "sayHello" : true,
                "sayGoodbye" : true
            });

            // Copy configured listeners into *this* object so 
            // that the base class's constructor will add them.
            this.listeners = config.listeners;

            // Call our superclass constructor to complete
            // construction process.
            this.callParent(arguments)
        }
    });

    var newEmployee = new Employee({
        name: "Neil",
        listeners: {
            sayHello: function() {
                // By default, "this" will be the object that
                // fired the event.
                console.log(this.name + " says Hello!");
            },
            sayGoodbye: function() {
                console.log(this.name + " says goodbye!");
            }
        }
    });

    // with the custom event defined and listener registered...
    // ...fire it up!
    newEmployee.fireEvent('sayHello');
    newEmployee.fireEvent('sayGoodbye');

});
*/
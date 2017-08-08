Ext.namespace("indicator");

Ext.regModel('namevalue', {
    fields: [
    	{name: 'id' }  ,
         {name: 'name' }  
    ]
});

Ext.regModel('responsevalue', {
    fields: [
    	{name: 'id' }  ,
         {name: 'name' }  ,
         {name: 'detail'}
    ]
});

Ext.regModel('indicatormodel',{
	fields: [
{ name: 'id'},
		{ name: 'indicators_detail_id'},
		{ name: 'detail'},
		{ name: 'target'},
		{ name: 'risk_section_id'},
		{ name: 'indicators_service_id'},
		{ name: 'indicator_value'},
		{ name: 'months_id'},
		{ name: 'years_id'}  		
	]
});


indicator.listIndicatorStore = new Ext.data.Store({
	model : 'indicatormodel',
	storeId:'listIndicatorStore',
	autoSync: true,
	proxy : {
		type: 'ajax',
		//type: 'rest',
		api: {
            read: '/indicator/listIndicatorBySection',
            create: '/indicator/createIndicator',
            update: '/indicator/updateIndicator',
            destroy: '/indicator/destroyIndicator'
        },
        reader: {
            type: 'json',
            successProperty: 'success',
            root: 'root',
            messageProperty: 'message'
        },
        writer: {
            type: 'json',
            writeAllFields: true,
            allowSingle :false,
            root: 'root'
        },
        listeners: {
            exception: function(proxy, response, operation){
                Ext.MessageBox.show({
                    title: 'REMOTE EXCEPTION',
                    msg: operation.getError(),
                    icon: Ext.MessageBox.ERROR,
                    buttons: Ext.Msg.OK
                });
            }
        }
	},
    listeners: {
        write: function(proxy, operation){
            if (operation.action == 'destroy') {
                main.child('#form').setActiveRecord(null);
            }
            
            this.reload();
        //    Ext.Msg.alert(operation.action, operation.resultSet.message);
        }
    },
	autoLoad : false
});

indicator.listYearsStore = new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/indicator/listYears',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

indicator.listMonthsStore = new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/indicator/listMonths',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

indicator.listAllRiskSection =   new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/indicator/listSection',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});


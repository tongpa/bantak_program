Ext.namespace("risks");

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
Ext.regModel('sectionteamtype', {
    fields: [
    	{name: 'id' }  ,
         {name: 'name' }  ,
         {name: 'type'} ,
         {name: 'type_name'},
         {name: 'eff'}
    ]
});

Ext.regModel('users', {
    fields: [
    	{name: 'id' }  ,
         {name: 'name' }  ,
         {name: 'display'} ,
         {name: 'email'} ,
         {name : 'group_id'},
         {name: 'group' }
    ]
});

Ext.regModel('risksmodel',{
	fields: [
		{ name: 'risk_management_id'},
		{ name: 'risk_detail'},
		{ name: 'risk_solution'},
		{ name: 'detail'},
		{ name: 'risk_level_id'},
		{ name: 'risk_section_id'},
		{ name: 'risk_status_id'},
		{ name: 'risk_program_group_id'},
		{ name: 'risk_program_detail_id'},
		{ name: 'report_date',type:'date' , dateFormat: 'Y-m-d H:i:s' },
		{ name: 'create_date',type:'date' , dateFormat: 'Y-m-d H:i:s' },
		{ name: 'risk_level'},
		{ name: 'level_desc'},
		{ name: 'risk_section'},
		{ name: 'risk_program_detail'},
		{ name: 'risk_program_group'},
		{ name: 'risk_status'},
		{ name: 'crom_team'},
		{ name: 'section_team'}

 		
	]
});


Ext.regModel('risksresponsemodel',{
	fields: [
		{ name: 'risk_management_id'},
		{ name: 'risk_detail'},
		{ name: 'detail'},
		{ name: 'risk_solution'},
		{ name: 'risk_team_id'},
		{ name: 'risk_level_id'},
		{ name: 'risk_section_id'},
		 
		{ name: 'risk_program_group_id'},
		{ name: 'risk_program_detail_id'},
		{ name: 'report_date',type:'date' , dateFormat: 'Y-m-d H:i:s' },
		 
		{ name: 'risk_level'},
		{ name: 'risk_section'},
		{ name: 'risk_program_detail'},
		{ name: 'risk_program_group'}  
	]
});


Ext.regModel('riskinmonth',{
	fields: [
		{ name: 'risk_management_id'},
		{ name: 'risk_detail'},
		{ name: 'risk_solution'},
		{ name: 'risk_section'},
		{ name: 'report_date',type:'date' , dateFormat: 'Y-m-d H:i:s' }
		 
	]
});

 
risks.listRiskLevel =   new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/risk/listRiskLevel',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});
 
risks.listRiskSection =   new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/risk/listSection',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

risks.listAllRiskSection =   new Ext.data.Store({
	model : 'namevalue',
	storeId:'listAllRiskSection',
	proxy: {
        type: 'ajax',
        url : '/risk/listSection',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

risks.listProgramGroup =   new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/risk/listProgramGroup',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

risks.listProgramDetail =   new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/risk/listProgramDetail',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

risks.listRiskStatus =   new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/risk/listRiskStatus',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

risks.listRiskStore = new Ext.data.Store({
	model : 'risksmodel',
	storeId:'listRiskStore',
	proxy : {
		type: 'ajax',
		url : '/risk/showRiskManage',
		reader : {
			type: 'json',
			root: 'root'
		}
	},
	autoLoad : false
});

risks.listRiskRespStore = new Ext.data.Store({
	model : 'risksmodel',//'risksresponsemodel',
	storeId:'listRiskRespStore',
	proxy : {
		type: 'ajax',
		url : '/risk/showRiskRespManage',
		reader : {
			type: 'json',
			root: 'root'
		}
	},
	autoLoad : false
});

risks.listSectionTeamStore = new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/risk/listTeamRespose?team_type=1',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

risks.listAcrossTeamStore = new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/risk/listTeamRespose?team_type=2',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

risks.findRiskResponsible = new Ext.data.Store({
	model : 'responsevalue',
	proxy: {
        type: 'ajax',
        url : '/risk/findRiskResponsible',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
}); 

risks.getUserStore = new Ext.data.Store({
	model : 'responsevalue',
	proxy :{
		type : 'ajax',
		url : '/risk/getUser',
		reader: {
			type : 'json',
			root : 'root'
		}
	},
    autoLoad: false
	//risks.getUserStore.data.items[0].data.id
});


risks.listInMonth = new Ext.data.Store({
	model : 'riskinmonth',
	storeId:'listInMonthStore',
	proxy :{
		type : 'ajax',
		url : '/risk/showDetailReportedByMonth',
		reader: {
			type : 'json',
			root : 'root'
		}
	},
    autoLoad: false
	//risks.getUserStore.data.items[0].data.id
});

risks.listSectionTeamType = new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/risk/listTeamResponseTypeAll',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});


risks.listSectionTeamAll = new Ext.data.Store({
	model : 'sectionteamtype',
	proxy: {
        type: 'ajax',
        url : '/risk/listTeamResponseAll',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

risks.listProgramsType = new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/risk/listProgramsTypeAll',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

risks.listProgramsAll = new Ext.data.Store({
	model : 'sectionteamtype',
	proxy: {
        type: 'ajax',
        url : '/risk/listProgramsAll',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

risks.listRiskLevelAll = new Ext.data.Store({
	model : 'sectionteamtype',
	proxy: {
        type: 'ajax',
        url : '/risk/listRiskLevelAll',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

risks.listUserAll = new Ext.data.Store({
	model : 'users',
	proxy: {
        type: 'ajax',
        url : '/risk/admin/listUser',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});

risks.listGroupUserAll = new Ext.data.Store({
	model : 'namevalue',
	proxy: {
        type: 'ajax',
        url : '/risk/admin/listGroupUser',
        reader: {
            type: 'json',
            root: 'root'
        }
    },
    autoLoad: false
});
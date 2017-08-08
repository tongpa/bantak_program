 
Ext.apply(Ext.form.field.VTypes, {
 
        password: function(val, field) {
            if (field.initialPassField) {
            	 
                var pwd = field.up('form').down('#' + field.initialPassField);
                return (val == pwd.getValue());
            }
            return true;
        },

        passwordText: 'รหัสผ่านไม่เหมือน'
    });


Ext.define('risks.gui.SectionRiskId',{
	extend : 'Ext.form.field.Hidden',
	alias : 'risk.section_id',
	name :'risk_section_id',
	value : ''
});
  
Ext.define('risks.gui.detailSection',{	 
	extend : 'Ext.form.field.Text',
	alias : 'risk.detail_section',
	name : 'detail_section',
	fieldLabel: 'รายละเอียด' ,
	allowBlank: false
});
   
Ext.define('risks.gui.SaveSectionButton',{
	extend : 'Ext.Button',
	alias : 'risk.saveButton',
	width : 100
});

Ext.define('risks.gui.DeleteSectionButton',{
	extend : 'Ext.Button',
	alias : 'risk.deleteButton',
	width : 100
});

Ext.define('risks.gui.ResetSectionButton',{
	extend : 'Ext.Button',
	alias : 'risk.resetButton',
	width : 100
});

//// section team 
Ext.define('risks.gui.SectionTeamId',{
	extend : 'Ext.form.field.Hidden',
	alias : 'risk.section_team_id',
	name :'id',
	value : ''
});

Ext.define('risks.gui.detailTeam',{	 
	extend : 'Ext.form.field.Text',
	alias : 'risk.detail_Team',
	name : 'name',
	fieldLabel: 'รายละเอียด' ,
	allowBlank: false
});

Ext.define('risks.gui.SectionTeamType',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'risk.teamType',
	name : 'type',
	//name : 'risk_team_type_id',
	fieldLabel: 'ประเภท',
	queryMode: 'local',
	forceSelection: true, 
	editable: false	,
    anchor: '100%',
    allowBlank: false, 
   // blankText :'กรุณาเลือกระดับ',
    displayField: 'name',
    valueField: 'id'	
});

/**programs **/
Ext.define('risks.gui.programsId',{
	extend : 'Ext.form.field.Hidden',
	alias : 'risk.programs_id',
	name :'id',
	value : ''
});

Ext.define('risks.gui.detailPrograms',{	 
	extend : 'Ext.form.field.Text',
	alias : 'risk.detail_Programs',
	name : 'name',
	fieldLabel: 'รายละเอียด' ,
	allowBlank: false
});

Ext.define('risks.guiProgramsType',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'risk.programsType',
	name : 'type',
	//name : 'risk_team_type_id',
	fieldLabel: 'ประเภท',
	queryMode: 'local',
	forceSelection: true, 
	editable: false	,
    anchor: '100%',
    allowBlank: false, 
   // blankText :'กรุณาเลือกระดับ',
    displayField: 'name',
    valueField: 'id'	
});


/**risk level **/
Ext.define('risks.gui.levelId',{
	extend : 'Ext.form.field.Hidden',
	alias : 'risk.level_id',
	name :'id',
	value : ''
});

Ext.define('risks.gui.detaillevel',{	 
	extend : 'Ext.form.field.Text',
	alias : 'risk.detail_level',
	name : 'name',
	fieldLabel: 'รายละเอียด' ,
	allowBlank: false
});

Ext.define('risks.gui.effective',{	 
	extend : 'Ext.form.field.Text',
	alias : 'risk.effective',
	name : 'eff',
	fieldLabel: 'ผลกระทบ' ,
	allowBlank: false
});

/**user **/
Ext.define('risks.gui.userId',{
	extend : 'Ext.form.field.Hidden',
	alias : 'risk.user_id',
	name :'id',
	value : ''
});

Ext.define('risks.gui.userName',{	 
	extend : 'Ext.form.field.Text',
	alias : 'risk.user_name',
	name : 'name',
	fieldLabel: 'login' ,
	allowBlank: false
});

Ext.define('risks.gui.userEmail',{	 
	extend : 'Ext.form.field.Text',
	alias : 'risk.user_email',
	name : 'email',
	fieldLabel: 'Email' ,
	allowBlank: false
});

Ext.define('risks.gui.userDisplay',{	 
	extend : 'Ext.form.field.Text',
	alias : 'risk.user_display',
	name : 'display',
	fieldLabel: 'ชื่อที่แสดง' ,
	allowBlank: false
});

Ext.define('risks.gui.userPassword',{	 
	extend : 'Ext.form.field.Text',
	alias : 'risk.user_password',
	name : 'password',
	itemId : 'password',
 	inputType : 'password',
	fieldLabel: 'รหัสผ่าน' 
});
Ext.define('risks.gui.userVPassword',{	 
	extend : 'Ext.form.field.Text',
	alias : 'risk.user_verify_password',
	name : 'verify_password',
 	inputType : 'password',
	fieldLabel: 'รหัสผ่านอีกครั้ง' ,
	vtype : 'password', 
	initialPassField : 'password'
});
Ext.define('risks.gui.userGroup',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'risk.userGroup',
	name : 'group_id',
	//name : 'risk_team_type_id',
	fieldLabel: 'ประเภท',
	queryMode: 'local',
	forceSelection: true, 
	editable: false	,
    anchor: '100%',
    allowBlank: false, 
   // blankText :'กรุณาเลือกระดับ',
    displayField: 'name',
    valueField: 'id'	
});

/**Section**/
Ext.define('risks.gui.GridSection',{
	extend : 'Ext.grid.Panel',
	alias : 'risk.gridSection',
	border :false,
	initComponent: function() {
    	var main = this;
    	this.store = risks.listRiskSection;
    	this.columns =  [
		    	       		{header: 'section id', dataIndex: 'id',width : '30%'  },  
		    	       		{header: 'หน่วยงาน',  dataIndex: 'name',width : '65%'}
		    	       		 
		    	        ] ;
		    	
    	this.callParent();
	}
});

/**Section team**/
Ext.define('risks.gui.GridSectionTeam',{
	extend : 'Ext.grid.Panel',
	alias : 'risk.gridSectionTeam',
	border :false,
	initComponent: function() {
    	var main = this;
    	this.store = risks.listSectionTeamAll;
    	this.columns =  [
		    	       		{header: 'id', dataIndex: 'id',width : '10%'  },  
		    	       		{header: 'ชื่อ',  dataIndex: 'name',width : '45%'},  
		    	       		{header: 'ประเภท',  dataIndex: 'type_name',width : '40%'}
		    	       		 
		    	        ] ;
		    	
    	this.callParent();
	}
});

/**programs**/
Ext.define('risks.gui.GridPrograms',{
	extend : 'Ext.grid.Panel',
	alias : 'risk.gridPrograms',
	border :false,
	initComponent: function() {
    	var main = this;
    	this.store = risks.listProgramsAll;
    	this.columns =  [
		    	       		{header: 'id', dataIndex: 'id',width : '8%'  },  
		    	       		{header: 'ชื่อ',  dataIndex: 'name',width : '60%'},  
		    	       		{header: 'ประเภท',  dataIndex: 'type_name',width : '32%'}
		    	       		 
		    	        ] ;
		    	
    	this.callParent();
	}
});

/**risk level**/
Ext.define('risks.gui.GridRiskLevel',{
	extend : 'Ext.grid.Panel',
	alias : 'risk.gridRiskLevel',
	border :false,
	initComponent: function() {
    	var main = this;
    	this.store = risks.listRiskLevelAll;
    	this.columns =  [
		    	       		{header: 'id', dataIndex: 'id',width : '8%'  },  
		    	       		{header: 'ชื่อ',  dataIndex: 'name',width : '10%'},  
		    	       		{header: 'ผลกระทบ',  dataIndex: 'eff',width : '48%'},  
		    	       		{header: 'ประเภท',  dataIndex: 'type_name',width : '32%'}
		    	       		 
		    	        ] ;
		    	
    	this.callParent();
	}
});

/**user**/
Ext.define('risks.gui.GridListUser',{
	extend : 'Ext.grid.Panel',
	alias : 'risk.gridListUser',
	border :false,
	initComponent: function() {
    	var main = this;
    	this.store = risks.listUserAll;
    	this.columns =  [
		    	       		 
		    	       		{header: 'ชื่อ',  dataIndex: 'name',width : '20%'},  
		    	       		{header: 'ชื่อที่แสดง',  dataIndex: 'display',width : '48%'},  
		    	       		{header: 'กลุ่ม',  dataIndex: 'group',width : '32%'}
		    	       		 
		    	        ] ;
		    	
    	this.callParent();
	}
});


/***Section**/
Ext.define('risks.view.ListSection', {
    extend: 'Ext.form.Panel',
    alias: 'risk.listSection',
    level : 0,
    loadStore :function(){
    	risks.listRiskSection.load();
    },
    saveSection : function(){
    	var main = this;    	
    	main.getForm().submit({
            url: '/risk/admin/saveSection',
            waitMsg: 'Please waiting...',
            success: function(fp1, o) {            	 
            	Ext.Msg.alert('บันทึก', 'บันทึกข้อมูลเรียบร้อย.' );
            	main.getForm().reset();           	
				main.loadStore();
	       	},
	       	failure: function (form, action) {
	       		//debugger;
                Ext.Msg.alert('Failed', action.result ? action.result.message : 'มีข้อมูลกรอกไม่สมบูรณ์');
            }
       }); 
    	
    },
    deleteSection : function(){
    	
    	var main = this;
    	main.detailSection.getValue()
    	Ext.Msg.confirm('ยินยัน', 'ต้องการลบรายการ '+ main.detailSection.getValue() + " นี้หรือไม่ ?", function(btn, text){
		       //alert(btn);
		       if(btn == 'yes')
		       {
		    	   main.getForm().submit({
		               url: '/risk/admin/deleteSection',
		               waitMsg: 'Please waiting...',
		               success: function(fp1, o) {	               	 
		             
		               	main.getForm().reset();		               	
		               	 
		   				main.loadStore();
		   	       	}
		          }); 
		       }
		    });
    },    
    initComponent: function() {
    	var main = this;
    	main.sectionid =    Ext.create('risks.gui.SectionRiskId' );
    	main.detailSection =     Ext.create('risks.gui.detailSection' );
    	main.gridSection =  Ext.create('risks.gui.GridSection', {anchor : '100%',
    		//title : 'หน่วยงาน',
			height : 400 ,
			listeners: {
                selectionchange: function(model, records) {
                    if (records[0]) {
                         main.sectionid.setValue( records[0].data.id);
                    	 main.detailSection.setValue( records[0].data.name);
                    }
                }
            }
         });
    	 
    	main.savesection =    Ext.create('risks.gui.SaveSectionButton', {text     : 'บันทึก',
    		listeners: {  click: function() { main.saveSection();  }	 }
    	});
    	
    	main.deletesection =    Ext.create('risks.gui.DeleteSectionButton', {text     : 'ลบรายการ',
    		listeners: {  click: function() { main.deleteSection();  }	 }
    	});
    	
    	main.reset =    Ext.create('risks.gui.ResetSectionButton', {text     : 'Reset',
    		listeners: {  click: function() {  main.form.reset();   }	 }
    	});
    	
    	
    	main.layoutsection = Ext.create('Ext.Panel',{
    		border : false,
    		autoWidth : true,
    		autoHeight : true,
    		anchor : '100%',
    		items : [
    		    {
    		    	xtype: 'fieldset',
    		    	title: 'หน่วยงาน',
    		    	defaults : {anchor:'98%'},
    		    	layout : 'anchor',
    		    	margin : '0 10 5 10',
    		    	items : [main.sectionid,main.detailSection
    		    	         ]
    		    }  ]   ,
    		    dockedItems :[{
    				xtype :'toolbar',
    				dock : 'bottom',
    				ui : 'footer',
    				layout : {
    					pack : 'center'
    				},
    				items : [main.savesection, main.deletesection, main.reset ]
    			}]
    	});
    	main.layout1 = Ext.create('Ext.Panel',{
			border : false,
			 
			autoWidth : true,
			anchor: '100%',
			layout:'column',
			//defaults:{margins:'0 5 5 0'},
			items : [
				{	
					layout: 'anchor',
					border : false,
					anchor: '100%',
					//bodyStyle: {  padding: '0px 10px' },
		    		columnWidth: .50,
		    		items : [ main.gridSection  ]
					 
				} ,
				{	
					layout: 'anchor',
					border : false,
					anchor: '100%',
				//	bodyStyle: { padding: '0px 10px' },
		    		columnWidth: .50,
					items : [main.layoutsection ]
				}   ]
		});
    	
    	this.items = [ main.layout1 ];
    	this.callParent();
    }
    
});


/**section team type**/
Ext.define('risks.view.ListSectionTeam', {
    extend: 'Ext.form.Panel',
    alias: 'risk.listSectionTeam',
    level : 0,
    loadStore :function(){
    	risks.listSectionTeamType.load();
    	risks.listSectionTeamAll.load();
    },
    saveSection : function(){
    	var main = this;    	
    	main.getForm().submit({
            url: '/risk/admin/saveSectionTeam',
            waitMsg: 'Please waiting...',
            success: function(fp1, o) {            	 
            	Ext.Msg.alert('บันทึก', 'บันทึกข้อมูลเรียบร้อย.' );
            	main.getForm().reset();           	
				main.loadStore();
	       	},
	       	failure: function (form, action) {
	       		//debugger;
                Ext.Msg.alert('Failed', action.result ? action.result.message : 'มีข้อมูลกรอกไม่สมบูรณ์');
            }
       }); 
    	
    },
    deleteSection : function(){
    	
    	var main = this; 
    	Ext.Msg.confirm('ยินยัน', 'ต้องการลบรายการ '+ main.detailTeam.getValue() + " นี้หรือไม่ ?", function(btn, text){
		       //alert(btn);
		       if(btn == 'yes')
		       {
		    	   main.getForm().submit({
		               url: '/risk/admin/deleteSectionTeam',
		               waitMsg: 'Please waiting...',
		               success: function(fp1, o) {	               	 
		             
		               	main.getForm().reset();		               	
		               	 
		   				main.loadStore();
		   	       	}
		          }); 
		       }
		    });
    },    
    initComponent: function() {
    	var main = this;
    	main.sectionTeamid =    Ext.create('risks.gui.SectionTeamId' );
    	main.detailTeam =     Ext.create('risks.gui.detailTeam' );
    	main.teamtype = Ext.create('risks.gui.SectionTeamType', {anchor : '98%',store:risks.listSectionTeamType});
    	
    	
    	main.gridSectionTeam =  Ext.create('risks.gui.GridSectionTeam', {anchor : '100%',
    		//title : 'หน่วยงาน',
			height : 400 ,
			listeners: {
                selectionchange: function(model, records) {
                    if (records[0]) {
                    	
                    	main.getForm().loadRecord(records[0]);
                         //main.sectionTeamid.setValue( records[0].data.id);
                    	 //main.detailTeam.setValue( records[0].data.name);
                    
                    }
                }
            }
         });
    	 
    	main.savesection =    Ext.create('risks.gui.SaveSectionButton', {text     : 'บันทึก',
    		listeners: {  click: function() { main.saveSection();  }	 }
    	});
    	
    	main.deletesection =    Ext.create('risks.gui.DeleteSectionButton', {text     : 'ลบรายการ',
    		listeners: {  click: function() { main.deleteSection();  }	 }
    	});
    	
    	main.reset =    Ext.create('risks.gui.ResetSectionButton', {text     : 'Reset',
    		listeners: {  click: function() {  main.form.reset();   }	 }
    	});
    	
    	
    	main.layoutsection = Ext.create('Ext.Panel',{
    		border : false,
    		autoWidth : true,
    		autoHeight : true,
    		anchor : '100%',
    		items : [
    		    {
    		    	xtype: 'fieldset',
    		    	title: 'หน่วยงาน/ทีมที่เกี่ยวข้อง',
    		    	defaults : {anchor:'98%'},
    		    	layout : 'anchor',
    		    	margin : '0 10 5 10',
    		    	items : [main.sectionTeamid,main.detailTeam,main.teamtype
    		    	         ]
    		    }  ]   ,
    		    dockedItems :[{
    				xtype :'toolbar',
    				dock : 'bottom',
    				ui : 'footer',
    				layout : {
    					pack : 'center'
    				},
    				items : [main.savesection, main.deletesection, main.reset ]
    			}]
    	});
    	main.layout1 = Ext.create('Ext.Panel',{
			border : false,
			 
			autoWidth : true,
			anchor: '100%',
			layout:'column',
			//defaults:{margins:'0 5 5 0'},
			items : [
				{	
					layout: 'anchor',
					border : false,
					anchor: '100%',
					//bodyStyle: {  padding: '0px 10px' },
		    		columnWidth: .50,
		    		items : [ main.gridSectionTeam  ]
					 
				} ,
				{	
					layout: 'anchor',
					border : false,
					anchor: '100%',
				//	bodyStyle: { padding: '0px 10px' },
		    		columnWidth: .50,
					items : [main.layoutsection ]
				}   ]
		});
    	
    	this.items = [ main.layout1 ];
    	this.callParent();
    }
    
});


/**program**/
Ext.define('risks.view.ListPrograms', {
    extend: 'Ext.form.Panel',
    alias: 'risk.listPrograms',
    level : 0,
    loadStore :function(){
    	risks.listProgramsType.load();
    	risks.listProgramsAll.load();
    },
    saveSection : function(){
    	var main = this;    	
    	main.getForm().submit({
            url: '/risk/admin/savePrograms',
            waitMsg: 'Please waiting...',
            success: function(fp1, o) {            	 
            	Ext.Msg.alert('บันทึก', 'บันทึกข้อมูลเรียบร้อย.' );
            	main.getForm().reset();           	
				main.loadStore();
	       	},
	       	failure: function (form, action) {
	       		//debugger;
                Ext.Msg.alert('Failed', action.result ? action.result.message : 'มีข้อมูลกรอกไม่สมบูรณ์');
            }
       }); 
    	
    },
    deleteSection : function(){
    	
    	var main = this; 
    	Ext.Msg.confirm('ยินยัน', 'ต้องการลบรายการ '+ main.detailprograms.getValue() + " นี้หรือไม่ ?", function(btn, text){
		       //alert(btn);
		       if(btn == 'yes')
		       {
		    	   main.getForm().submit({
		               url: '/risk/admin/deletePrograms',
		               waitMsg: 'Please waiting...',
		               success: function(fp1, o) {	               	 
		             
		               	main.getForm().reset();		               	
		               	 
		   				main.loadStore();
		   	       	}
		          }); 
		       }
		    });
    },    
    initComponent: function() {
    	var main = this;
    	main.programsid =    Ext.create('risks.gui.programsId' );
    	main.detailprograms =     Ext.create('risks.gui.detailPrograms' );
    	main.programstype = Ext.create('risks.guiProgramsType', {anchor : '98%',store:risks.listProgramsType});
    	
    	
    	main.gridPrograms =  Ext.create('risks.gui.GridPrograms', {anchor : '100%',
    		//title : 'หน่วยงาน',
			height : 400 ,
			listeners: {
                selectionchange: function(model, records) {
                    if (records[0]) {
                    	
                    	main.getForm().loadRecord(records[0]);
                         //main.sectionTeamid.setValue( records[0].data.id);
                    	 //main.detailTeam.setValue( records[0].data.name);
                    
                    }
                }
            }
         });
    	 
    	main.savesection =    Ext.create('risks.gui.SaveSectionButton', {text     : 'บันทึก',
    		listeners: {  click: function() { main.saveSection();  }	 }
    	});
    	
    	main.deletesection =    Ext.create('risks.gui.DeleteSectionButton', {text     : 'ลบรายการ',
    		listeners: {  click: function() { main.deleteSection();  }	 }
    	});
    	
    	main.reset =    Ext.create('risks.gui.ResetSectionButton', {text     : 'Reset',
    		listeners: {  click: function() {  main.form.reset();   }	 }
    	});
    	
    	
    	main.layoutsection = Ext.create('Ext.Panel',{
    		border : false,
    		autoWidth : true,
    		autoHeight : true,
    		anchor : '100%',
    		items : [
    		    {
    		    	xtype: 'fieldset',
    		    	title: 'ด้าน/โปรแรกม',
    		    	defaults : {anchor:'98%'},
    		    	layout : 'anchor',
    		    	margin : '0 10 5 10',
    		    	items : [main.programsid,main.detailprograms,main.programstype
    		    	         ]
    		    }  ]   ,
    		    dockedItems :[{
    				xtype :'toolbar',
    				dock : 'bottom',
    				ui : 'footer',
    				layout : {
    					pack : 'center'
    				},
    				items : [main.savesection, main.deletesection, main.reset ]
    			}]
    	});
    	main.layout1 = Ext.create('Ext.Panel',{
			border : false,
			 
			autoWidth : true,
			anchor: '100%',
			layout:'column',
			//defaults:{margins:'0 5 5 0'},
			items : [
				{	
					layout: 'anchor',
					border : false,
					anchor: '100%',
					//bodyStyle: {  padding: '0px 10px' },
		    		columnWidth: .50,
		    		items : [ main.gridPrograms  ]
					 
				} ,
				{	
					layout: 'anchor',
					border : false,
					anchor: '100%',
				//	bodyStyle: { padding: '0px 10px' },
		    		columnWidth: .50,
					items : [main.layoutsection ]
				}   ]
		});
    	
    	this.items = [ main.layout1 ];
    	this.callParent();
    }
    
});

/**risk level**/
Ext.define('risks.view.ListRiskLevel', {
    extend: 'Ext.form.Panel',
    alias: 'risk.listRiskLevel',
    level : 0,
    loadStore :function(){
    	risks.listProgramsType.load();
    	risks.listRiskLevelAll.load();
    },
    saveSection : function(){
    	var main = this;    	
    	main.getForm().submit({
            url: '/risk/admin/saveRiskLevel',
            waitMsg: 'Please waiting...',
            success: function(fp1, o) {            	 
            	Ext.Msg.alert('บันทึก', 'บันทึกข้อมูลเรียบร้อย.' );
            	main.getForm().reset();           	
				main.loadStore();
	       	},
	       	failure: function (form, action) {
	       		//debugger;
                Ext.Msg.alert('Failed', action.result ? action.result.message : 'มีข้อมูลกรอกไม่สมบูรณ์');
            }
       }); 
    	
    },
    deleteSection : function(){
    	
    	var main = this; 
    	Ext.Msg.confirm('ยินยัน', 'ต้องการลบรายการ '+ main.detailprograms.getValue() + " นี้หรือไม่ ?", function(btn, text){
		       //alert(btn);
		       if(btn == 'yes')
		       {
		    	   main.getForm().submit({
		               url: '/risk/admin/deleteRiskLevel',
		               waitMsg: 'Please waiting...',
		               success: function(fp1, o) {	               	 
		             
		               	main.getForm().reset();		               	
		               	 
		   				main.loadStore();
		   	       	}
		          }); 
		       }
		    });
    },    
    initComponent: function() {
    	var main = this;
    	main.programsid =    Ext.create('risks.gui.levelId' );
    	main.detailprograms =     Ext.create('risks.gui.detaillevel' );
    	main.effective=     Ext.create('risks.gui.effective' );
    	main.programstype = Ext.create('risks.guiProgramsType', {anchor : '98%',store:risks.listProgramsType});
    	
    	
    	main.gridPrograms =  Ext.create('risks.gui.GridRiskLevel', {anchor : '100%',
    		//title : 'หน่วยงาน',
			height : 400 ,
			listeners: {
                selectionchange: function(model, records) {
                    if (records[0]) {
                    	
                    	main.getForm().loadRecord(records[0]);
                         //main.sectionTeamid.setValue( records[0].data.id);
                    	 //main.detailTeam.setValue( records[0].data.name);
                    
                    }
                }
            }
         });
    	 
    	main.savesection =    Ext.create('risks.gui.SaveSectionButton', {text     : 'บันทึก',
    		listeners: {  click: function() { main.saveSection();  }	 }
    	});
    	
    	main.deletesection =    Ext.create('risks.gui.DeleteSectionButton', {text     : 'ลบรายการ',
    		listeners: {  click: function() { main.deleteSection();  }	 }
    	});
    	
    	main.reset =    Ext.create('risks.gui.ResetSectionButton', {text     : 'Reset',
    		listeners: {  click: function() {  main.form.reset();   }	 }
    	});
    	
    	
    	main.layoutsection = Ext.create('Ext.Panel',{
    		border : false,
    		autoWidth : true,
    		anchor : '100%',
    		items : [
    		    {
    		    	xtype: 'fieldset',
    		    	title: 'ระดับความรุนแรง',
    		    	defaults : {anchor:'98%'},
    		    	layout : 'anchor',
    		    	margin : '0 10 5 10',
    		    	items : [main.programsid,main.detailprograms,main.effective,main.programstype
    		    	         ]
    		    }  ]   ,
    		    dockedItems :[{
    				xtype :'toolbar',
    				dock : 'bottom',
    				ui : 'footer',
    				layout : {
    					pack : 'center'
    				},
    				items : [main.savesection, main.deletesection, main.reset ]
    			}]
    	});
    	main.layout1 = Ext.create('Ext.Panel',{
			border : false,
			 
			autoWidth : true,
			anchor: '100%',
			layout:'column',
			//defaults:{margins:'0 5 5 0'},
			items : [
				{	
					layout: 'anchor',
					border : false,
					anchor: '100%',
					//bodyStyle: {  padding: '0px 10px' },
		    		columnWidth: .50,
		    		items : [ main.gridPrograms  ]
					 
				} ,
				{	
					layout: 'anchor',
					border : false,
					anchor: '100%',
				//	bodyStyle: { padding: '0px 10px' },
		    		columnWidth: .50,
					items : [main.layoutsection ]
				}   ]
		});
    	
    	this.items = [ main.layout1 ];
    	this.callParent();
    }
    
});


/**User **/
Ext.define('risks.view.ListUser', {
    extend: 'Ext.form.Panel',
    alias: 'risk.listUser',
    level : 0,
    loadStore :function(){
    	risks.listUserAll.load();
    	risks.listGroupUserAll.load();
    },
    saveSection : function(){
    	var main = this;    	
    	
    	
    	
    	
    	main.getForm().submit({
            url: '/risk/admin/saveUser',
            waitMsg: 'Please waiting...',
            success: function(fp1, o) {            	 
            	Ext.Msg.alert('บันทึก', 'บันทึกข้อมูลเรียบร้อย.' );
            	main.getForm().reset();           	
				main.loadStore();
	       	},
	       	failure: function (form, action) {
	       		//debugger;
                Ext.Msg.alert('Failed', action.result ? action.result.message : 'มีข้อมูลกรอกไม่สมบูรณ์');
            }
       }); 
    	
    },
    deleteSection : function(){
    	
    	var main = this; 
    	Ext.Msg.confirm('ยินยัน', 'ต้องการลบรายการ '+ main.userName.getValue() + " นี้หรือไม่ ?", function(btn, text){
		       //alert(btn);
		       if(btn == 'yes')
		       {
		    	   main.getForm().submit({
		               url: '/risk/admin/deleteUser',
		               waitMsg: 'Please waiting...',
		               success: function(fp1, o) {	               	 
		             
		               	main.getForm().reset();		               	
		               	 
		   				main.loadStore();
		   	       	}
		          }); 
		       }
		    });
    },    
    initComponent: function() {
    	var main = this;
    	main.userId =    Ext.create('risks.gui.userId' );
    	main.userName =     Ext.create('risks.gui.userName' );
    	main.userEmail=     Ext.create('risks.gui.userEmail' );
    	main.userDisplay=     Ext.create('risks.gui.userDisplay' );
    	main.userPassword=     Ext.create('risks.gui.userPassword' );
    	main.userVPassword=     Ext.create('risks.gui.userVPassword' ); 
    	
    	
    	main.programstype = Ext.create('risks.gui.userGroup', {anchor : '98%',store:risks.listGroupUserAll});
    	
    	
    	main.gridPrograms =  Ext.create('risks.gui.GridListUser', {anchor : '100%',
    		//title : 'หน่วยงาน',
			height : 400 ,
			listeners: {
                selectionchange: function(model, records) {
                    if (records[0]) {
                    	
                    	main.getForm().loadRecord(records[0]);
                         //main.sectionTeamid.setValue( records[0].data.id);
                    	 //main.detailTeam.setValue( records[0].data.name);
                    
                    }
                }
            }
         });
    	 
    	main.savesection =    Ext.create('risks.gui.SaveSectionButton', {text     : 'บันทึก',
    		listeners: {  click: function() { main.saveSection();  }	 }
    	});
    	
    	main.deletesection =    Ext.create('risks.gui.DeleteSectionButton', {text     : 'ลบรายการ',
    		listeners: {  click: function() { main.deleteSection();  }	 }
    	});
    	
    	main.reset =    Ext.create('risks.gui.ResetSectionButton', {text     : 'Reset',
    		listeners: {  click: function() {  main.form.reset();   }	 }
    	});
    	
    	
    	main.layoutsection = Ext.create('Ext.Panel',{
    		border : false,
    		autoWidth : true,
    		autoHeight : true,
    		anchor : '100%',
    		items : [
    		    {
    		    	xtype: 'fieldset',
    		    	title: 'ผู้ใช้งาน',
    		    	defaults : {anchor:'98%'},
    		    	layout : 'anchor',
    		    	margin : '0 10 5 10',
    		    	items : [main.userId,main.userName,main.userEmail,main.userDisplay,main.userPassword,main.userVPassword,main.programstype
    		    	         ]
    		    }  ]   ,
    		    dockedItems :[{
    				xtype :'toolbar',
    				dock : 'bottom',
    				ui : 'footer',
    				 
    				layout : {
    					pack : 'center'
    				},
    				items : [main.savesection, main.deletesection, main.reset ]
    			}]
    	});
    	main.layout1 = Ext.create('Ext.Panel',{
			border : false,
			 
			autoWidth : true,
			anchor: '100%',
			layout:'column',
			//defaults:{margins:'0 5 5 0'},
			items : [
				{	
					layout: 'anchor',
					border : false,
					anchor: '100%',
					//bodyStyle: {  padding: '0px 10px' },
		    		columnWidth: .50,
		    		items : [ main.gridPrograms  ]
					 
				} ,
				{	
					layout: 'anchor',
					border : false,
					anchor: '100%',
				//	bodyStyle: { padding: '0px 10px' },
		    		columnWidth: .50,
					items : [main.layoutsection ]
				}   ]
		});
    	
    	this.items = [ main.layout1 ];
    	this.callParent();
    }
    
});
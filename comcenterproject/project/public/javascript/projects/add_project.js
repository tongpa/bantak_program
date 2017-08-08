Ext.namespace("projects");
Ext.namespace("maintenance");

Ext.apply(Ext.form.field.VTypes, {
        daterange: function(val, field) {
            var date = field.parseDate(val);

            if (!date) {
                return false;
            }
            if (field.startDateField && (!this.dateRangeMax || (date.getTime() != this.dateRangeMax.getTime()))) {
                var start = field.up('form').down('#' + field.startDateField);
                start.setMaxValue(date);
                start.validate();
                this.dateRangeMax = date;
            }
            else if (field.endDateField && (!this.dateRangeMin || (date.getTime() != this.dateRangeMin.getTime()))) {
                var end = field.up('form').down('#' + field.endDateField);
                end.setMinValue(date);
                end.validate();
                this.dateRangeMin = date;
            }
            /*
             * Always return true since we're only using this vtype to set the
             * min/max allowed values (these are tested for after the vtype test)
             */
            return true;
        },

        daterangeText: 'Start date must be less than end date' 
    });

projects.AddProject = Ext.extend(Ext.form.Panel,{
//	title : 'แบบฟอร์ม',
	fromedit : false, 
	width : 490,
	height : 500 ,
	fromWin: null,
	fromMain: null,
	currentRecord : null,
	setLoadData : function(record){
		this.getForm().loadRecord(record);
		this.currentRecord = record;
		if(record.data.plantype_id == 1) 
		{
			this.inPlan.setValue(true);
			this.outPlan.setValue(false);
		}
		else{
			this.inPlan.setValue(false);
			this.outPlan.setValue(true);
		}
		//debugger;
		
	},
	setFromView : function(visible){
		this.status.setVisible(true);
		this.deleteProject.setVisible(false);
		this.save.setVisible(false);
	},
	setFormEdit : function(visible){
		//debugger;
		this.status.setVisible(visible);//false
		this.deleteProject.setVisible(visible);
	},
	initComponent: function( ) {
		var main = this;
		
		var today = new Date();
		/*var offset = 7;//bangkok 
		utc = today.getTime() + (today.getTimezoneOffset() * 60000);
		nd = new Date(utc + (3600000*offset)); //nd.toLocaleString()*/
		
		year = Ext.Date.format(today, 'Y');
		year = parseInt(year, 10) +543;
		
		year = parseInt(year, 10) +1; //next 1 year 
	 
		main.projectName = new Ext.form.field.Text({
			name:'project_name',
			fieldLabel : 'ชื่อโครงการ',
			allowBlank: false,
			anchor: '100%',
			blankText :'กรุณากรอกชื่อโครงการ'
		});
		
		main.userName = new Ext.form.field.Text({
			name:'user_name',
			fieldLabel : 'ชื่อผู้รับผิดชอบ',
			allowBlank: false,
			anchor: '100%',
			blankText :'กรุณากรอกชื่อผู้รับผิดชอบ'
		});
		
		main.projectId = new Ext.form.field.Hidden({
			name : 'project_id',
			anchor:'100%',
			value : ''
		});
		
		
		main.detail = new Ext.form.field.TextArea({
			grow      : true,
	        name      : 'detail',
	        fieldLabel: 'รายละเอียด',
	        anchor    : '100%'
				
		});
		main.fiscalyear = new Ext.form.field.Number({
			anchor: '50%',
	        name: 'fiscal_year',
	        fieldLabel: 'ปีงบประมาณ',
	        value : year,
	        maxValue: 2600,
        	minValue: 2553				
		});
		main.budget = new Ext.form.field.Number({
			anchor: '50%',
	        name: 'project_budget',
	        fieldLabel: 'เงินงบประมาณ',
	        hideTrigger: true,
	        keyNavEnabled: false,
	        mouseWheelEnabled: false,
	        value : 0				
		});
		
		main.maintenanceFundsBudget = new Ext.form.field.Number({
			anchor: '50%',
	        name: 'maintenance_funds_budget',
	        fieldLabel: 'เงินบำรุง',
	        hideTrigger: true,
	        keyNavEnabled: false,
	        mouseWheelEnabled: false,
	        value : 0				
		});
		
		main.budget_other = new Ext.form.field.Number({
			anchor: '50%',
	        name: 'budget_other',
	        fieldLabel: 'เงินงบประมาณอื่น',
	        hideTrigger: true,
	        keyNavEnabled: false,
	        mouseWheelEnabled: false,
	        value : 0,
	        listeners : {
	        	change: function(field, value) {
	        		 
	        		if(value == null){ 
	        			value = 0;
	        			field.setValue(0);
	        		}
                	value = parseInt(value, 10);
                	 
                	main.budget_other_from.setDisabled(true);
                	if(value > 0)
                	{
                		main.budget_other_from.setDisabled(false);
                	}
                	
            	}
	        	 
	        }
				
		});
		main.budget_other_from = new Ext.form.field.TextArea({
			grow      : false,
	        name      : 'budget_other_from',
	        fieldLabel: 'จาก',
	        allowBlank: false, 
	        disabled  : true,
	        anchor    : '100%',
	        growMin :30, 
	        growMax :60,
	        height : 30,
			blankText :'กรุณากรอก ที่มาของเงินงบประมาณอื่น'
				
		});
		main.projectType = new Ext.form.field.ComboBox({
			fieldLabel: 'ประเภท',
			name : 'projectType',
		    store: projects.listProjectType,
		    queryMode: 'local',
		    displayField: 'name',
		    valueField: 'id'	,
		    value : '*',
		    editable: false	,
		    anchor: '100%',
		    allowBlank: false, 
		    blankText :'กรุณาเลือกประเภทโครงการ'
		});
		
		main.division= new Ext.form.field.ComboBox({
			fieldLabel: 'แผนก/ฝ่าย',
			name : 'division_id', 
		    store: maintenance.listDivision,
		    queryMode: 'local',
		    displayField: 'name',
		    valueField: 'id'	,
		    value : '*',
		    editable: false	,
		    anchor: '100%',
		    listeners:{
		         scope: this,
		         'select': function (  field,   value,   options ){
		         	main.section.reset();
		         	division = value[0].data.id;
		         	projects.listSection.load({
		         		params : {
		         			division : division
		         		}
		         	});
		         	 
		         }
		    }
		});
		main.section = new Ext.form.field.ComboBox({
			fieldLabel: 'หน่วย/งาน',
			name : 'section_id', 
		    store: projects.listSection,
		    queryMode: 'local',
		    displayField: 'name',
		    valueField: 'id'	,
		    value : '*',
		    editable: false	,
		    anchor: '100%'
		});
		main.startDate = new Ext.form.field.Date({
			fieldLabel: 'วันที่เริ่มโครงการ',
			anchor: '50%',
	        name: 'start_date',
	        id : 'start_date',
	       value: new Date(),  
	        format: 'd/m/Y',
	        vtype: 'daterange',
	        endDateField: 'stop_date' 
		});
		
		main.stopDate = new Ext.form.field.Date({
			fieldLabel: 'วันที่สิ้นสุดโครงการ',
			anchor: '50%',	        
	        name: 'stop_date',
	        id :  'stop_date',
	        
	        format: 'd/m/Y',
	        vtype: 'daterange',
	        startDateField: 'start_date'
		});
		
		main.inPlan= new Ext.form.field.Radio({
			boxLabel: 'ในแผน', name: 'planType', inputValue: '1',checked: true
		});
		main.outPlan  = new Ext.form.field.Radio({
			boxLabel: 'นอกแผน', name: 'planType', inputValue: '2'
		});
		
		main.planType = new Ext.form.RadioGroup({
			 
			fieldLabel: 'แผนโครงการ',
			items: [
            	main.inPlan,
            	main.outPlan
            ]
		});
		main.status = new Ext.form.field.ComboBox({
			fieldLabel: 'สถานะ',
			name : 'project_status_id', 
		    store: projects.listStatus,
		    queryMode: 'local',
		    displayField: 'name',
		    valueField: 'id'	,
		    value : '*',
		    editable: false	,
		    anchor: '100%'
		    
		});
		
		main.close = new Ext.Button({
			text : 'ปิด',
			width : 120,
			listeners : {
				click : function (){
					if( main.fromWin != null ){
						 
						main.fromWin.hide();
						
					}
				}
			}
		});
		
		main.deleteProject = new Ext.Button({
			text : 'ยกเลิก',
			width : 120,
			listeners : {
				click : function(){
					Ext.MessageBox.confirm('Confirm', 'ต้องการจะลบรายการนี้หรือไม่?', function result(btn){
						if(btn == 'yes'){
							main.getForm().submit({
				                url: '/project/deleteProject',
				                waitMsg: 'Please waiting...',
				                success: function(fp1, o) {
				                	Ext.Msg.alert('ลบ', 'ลบรายการเสร็จเรียบร้อย.' );
				                	main.getForm().reset();
				                	if( main.fromWin != null ){
										main.fromWin.hide();
									}
									 
									projects.listProjectStore.remove(main.currentRecord);
									main.currentRecord = null;
									//debugger;
						       	}
					       }); 
						}
					} );
				}
			}
		});
		main.save = new Ext.Button({
			text     : 'บันทึก',
			width : 120,
			listeners: {
		        click: function() {
		            //this == the button, as we are in the local scope
		           // this.setText('I was clicked!');
		           main.getForm().submit({
		                url: '/project/createProject',
		                waitMsg: 'Please waiting...',
		                success: function(fp1, o) {
		                	//alert("success");
		                	//o.result.message
		                	//debugger;
		                	Ext.Msg.alert('บันทึก', 'บันทึกเสร็จเรียบร้อย.' );
		                	main.getForm().reset();
		                	if( main.fromWin != null ){
								main.fromWin.hide();
							}
							if(main.fromMain != null){
								main.fromMain.loadDataSearch();
							}
							//projects.listProjectStore.reload();
				       	}
			       }); 
			     }  
		       /*, mouseover: function() {
		            //set a new config which says we moused over, if not already set
		            if (!this.mousedOver) {
		                this.mousedOver = true;
		                alert('You moused over a button!\n\nI wont do this again.');
		            }
		        }*/
		    }
					
		});
		
		Ext.apply(this, {
			bodyPadding: 10,
			 
			items : [main.projectId,main.projectType,main.fiscalyear,main.planType,main.projectName,main.userName,main.division,main.section,main.budget,main.maintenanceFundsBudget,main.budget_other,main.budget_other_from, main.startDate,main.stopDate,main.detail,main.status ],
			 
			dockedItems :[{
				xtype :'toolbar',
				dock : 'bottom',
				ui : 'footer',
				layout : {
					pack : 'center'
				},
				items : [
					main.deleteProject,'->','->', main.save,main.close
				]
			}]	 
		});
		projects.AddProject.superclass.initComponent.apply(this, arguments);
	}
	
	/*
	items :[
		{
			xtype: 'datefield',
	        anchor: '100%',
	        fieldLabel: 'From',
	        name: 'from_date',
	        maxValue: new Date() 
		
		}
	]*/
});
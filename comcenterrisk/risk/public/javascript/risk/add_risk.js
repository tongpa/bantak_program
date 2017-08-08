 
Ext.define('risks.gui.RiskId',{
	extend : 'Ext.form.field.Hidden',
	alias : 'risk.riskId',
	name :'risk_management_id',
	value : ''
});

Ext.define('risks.gui.LevelId',{
	extend : 'Ext.form.field.Hidden',
	alias : 'risk.levelId',
	name :'level',
	value : '0'
});

Ext.define('risks.gui.reportDate',{
	extend : 'Ext.form.field.Date',
	alias : 'risk.reportDate',
	name :'report_date',
	fieldLabel: 'วันที่พบเหตุการณ์',
	value : new Date(),
	format: 'd/m/Y'
});

Ext.define('risks.gui.detailRisk',{
	 extend : 'Ext.form.field.TextArea',
	//extend : 'Ext.form.field.Text',
	alias : 'risk.detailRisk',
	name : 'detail',
	fieldLabel: 'รายละเอียด',
	maxHeight : 80,
	height : 70,
	grow      : false
});
 
Ext.define('risks.gui.solutionRisk',{
	 extend : 'Ext.form.field.TextArea',
	//extend : 'Ext.form.field.Text',
	alias : 'risk.solutionRisk',
	name : 'risk_solution',
	fieldLabel: 'แนวทางการแก้ไข',
	maxHeight : 80,
	height : 70,
	grow      : false
});

Ext.define('risks.gui.RiskLevel',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'risk.risklevel',
	name : 'risk_level_id',
	fieldLabel: 'ระดับ',
	queryMode: 'local',
	forceSelection: true, 
	editable: false	,
    anchor: '100%',
    allowBlank: false, 
    blankText :'กรุณาเลือกระดับ',
    displayField: 'name',
    valueField: 'id'	
});

Ext.define('risks.gui.RiskSection',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'risk.riskSection',
	name : 'risk_section_id',
	queryMode: 'local',
	forceSelection: true, 
	fieldLabel: 'หน่วยงาน',
	editable: false	,
    anchor: '100%',
    allowBlank: false,   
    blankText :'กรุณาเลือกหน่วยงานที่รายงาน',
    displayField: 'name',
    valueField: 'id'	
});

Ext.define('risks.gui.RiskProgramDetail',{
	extend : 'Ext.form.field.ComboBox',
	alias : 'risk.riskProgramDetail',
	name : 'risk_program_detail_id',
	fieldLabel: 'ด้าน/โปรแกรม',
	queryMode: 'local',
	forceSelection: true, 
	editable: false	,
    anchor: '100%',
    allowBlank: false, 
    blankText :'กรุณาเลือกด้าน/โปรแกรม',
    displayField: 'name',
    valueField: 'id'	
});

Ext.define('risk.gui.BtClose',{
	extend : 'Ext.Button',
	alias : 'risk.bt.Close', 
	html : '<b>ปิด</b>',
	scale   : 'large',
	width : 120,
	fromWin : null,
	listeners : {
		click : function (){
			if( this.fromWin != null ){
				this.fromWin.hide();
			}
		}
	}
	
});
 
Ext.define('risk.gui.TextSection',{
	extend : 'Ext.form.Label',
	alias : 'risk.TextSection', 
	text: ' ', 
	//width : 120,
	forId: 'myFieldId'	
});

Ext.define('risk.gui.TextProgramGroup',{
	extend : 'Ext.form.Label',
	alias : 'risk.TextProgramGroup', 
	text: ' ' 
	//width : 120,
	//forId: 'myFieldId'	
});

Ext.define('risk.gui.TextRiskProgramDetail',{
	extend : 'Ext.form.Label',
	alias : 'risk.TextRiskProgramDetail', 
	text: ' ' 
	//width : 120,
	//forId: 'myFieldId'	
});
 

Ext.define('risk.gui.TextRiskLevel',{
	extend : 'Ext.form.Label',
	alias : 'risk.TextRiskLevel', 
	text: ' ' 
	//width : 120,
	//forId: 'myFieldId'	
});
 

Ext.define('risks.gui.RiskProgramGroup',{
	extend : 'Ext.form.RadioGroup',
	alias : 'risk.riskProgramGroup',
	columns : 2,
	vertical : true,
	tempValue : 1,
	fieldLabel: 'ประเภท',
	clickRadio:null,
	mainObject:null,
	initComponent:function(){
		var main = this;
		 
		
		main.clinic = new Ext.form.field.Radio({
			main:main.mainObject,boxLabel: 'โปรแกรมทางคลินิก', name: 'risk_program', inputValue: '1'  , checked: true,handler: main.clickRadio
		}); 
		main.phycal = new Ext.form.field.Radio({
			main:main.mainObject,boxLabel: 'โปรแกรมทางกายภาพ', name: 'risk_program', inputValue: '2',handler: main.clickRadio
		}); 
		this.items = [main.clinic,main.phycal];
		
		this.callParent();
	},
	forloadData: function(inputValue){
		var main = this;
		if(inputValue == 1){
			main.clinic.setValue(true);
			main.phycal.setValue(false);
		}
		else{
			main.clinic.setValue(false);
			main.phycal.setValue(true);
		}
	}
});

Ext.define('risks.gui.SectionTeam',{
	extend : 'Ext.panel.Panel',
	alias :'risk.SectionTeam',

	border : false,
	anchor: '100%',
	layout:'column',
	getLengthSectionTeam : function(){
		return this.sectionTeam.getValue().length;
	},
	getLengthCromTeam : function(){
		return this.cromTeam.getValue().length
	},
	initComponent: function() {
    	var main = this; 
    	
    	main.sectionTeam = new Ext.ux.form.ItemSelector({
			name: 'section_team',
            anchor: '100%',
            fieldLabel: 'หน่วยงาน',
            imagePath: '/ux/images/',
			labelWidth : 60, 
            store: risks.listSectionTeamStore,
            displayField: 'name',
            valueField: 'id',
            //value: ['3', '4', '6'],
			columnWidth: .50,
			height:200,
            allowBlank: true, 
            msgTarget: 'side' 
            
		});
    	 
    	 
		main.cromTeam = new Ext.ux.form.ItemSelector({
			name: 'crom_team',
            anchor: '100%',
            fieldLabel: 'ทีมคร่อม',
            imagePath: '/ux/images/',
			labelWidth : 60, 
            store: risks.listAcrossTeamStore,
            displayField: 'name',
            valueField: 'id',
            height:200,
			columnWidth: .50,
            allowBlank: true, 
            msgTarget: 'side'
		}); 
     
    	 
		this.items = [main.sectionTeam ,main.cromTeam ];
    	
     
    	
    	this.callParent();
	}
});

Ext.define('risk.view.PanelResponseRisk',{
	extend : 'Ext.panel.Panel',
	alias : 'risk.panelResponseRisk', 
	textid : null,
	field_label : "",
	text_detail : "",
	 
	initComponent: function( ) {
		var main = this;
		this.addEvents({ deleteMe: true });
		main.deleteBt = new Ext.Button({
			 
			tooltip:'ลบรายการ :'+main.field_label,
			icon: '/images/delete.png',			
			name :  main.textid,
			listeners: {
		        click: function() {
		        	 Ext.Msg.confirm('ยินยัน', 'ต้องการลบรายการ '+ main.field_label + " นี้หรือไม่ ?", function(btn, text){
					       //alert(btn);
					       if(btn == 'yes')
					       {
					       	main.fireEvent('deleteMe',main);
					       }
					    });
 					 
			     }  
		       
		    }
					
		});
		main.deleteBt.setVisible(false);
		main.obj1 = new Ext.form.field.TextArea({
				grow      : true,
		        name      : 'details'+main.textid ,
		        fieldLabel: main.field_label,
		        anchor    : '100%',
		       // anchor    : '100%  -47'	,
		        value     :  main.text_detail 
			});
		 
		
		Ext.apply(this, {
			border : false,
			anchor: '100%',	
			//bodyPadding: 10 ,
			layout:'column',
			//defaults:{margins:'0 5 5 0'},
			items : [
				{
					border : false,
					columnWidth: .95,
					layout: 'anchor',
					items:[main.obj1]
				},
				{
					border : false,
					columnWidth: .05,
					layout: 'anchor',
					items:[main.deleteBt]
				}
			]
			 
			 	 
		});
		
		this.callParent();
	}
});

Ext.define('risk.view.ResponseRisk',{
	extend : 'Ext.form.Panel',
	alias : 'risk.responseRisk',
	resetAll :function(){
		this.removeAll(true); 
	},
	bodyPadding: 10, 
	border : false,
	setLoadData : function(record){
		var main = this;
		var section_team = record.data.section_team;
		var cron_team = record.data.crom_team;
		var len = risks.listSectionTeamStore.data.length;
		var data = risks.listSectionTeamStore.data;
		 
		
		this.removeAll(true); 
		this.doLayout();
		var teams =  "";
		for(var i in section_team) {
			var steam = section_team[i];
			for (var r=0 ; r < len;r++){
				var value =  data.items[r];
				if(value.data.id == steam)
				{
					teams =teams +steam + "," ;
		 		
					 
					break;
				}
			} 
		}
		var len = risks.listAcrossTeamStore.data.length;
		var data = risks.listAcrossTeamStore.data;
		for(var i in cron_team) {
			var steam = cron_team[i];
			for (var r=0 ; r < len;r++){
				var value =  data.items[r];
				if(value.data.id == steam)
				{
					teams =teams +steam + "," ;
 				 
					break;
				}
			} 
		}
		if(teams.length >=1)
			teams = teams.substring(0,(teams.length-1) );
	
		risks.findRiskResponsible.load({
			params : {
     			 risk_team : teams,
     			 risk_namager:record.data.risk_management_id
     		},
     		callback: function(records, o, s) {
                if (s) {
                	 
                	var leng = records.length;
                	for (var row=0 ; row< leng ; row++)
                	{
                		 
                		var obj1= Ext.create('risk.view.PanelResponseRisk',{
                			textid : records[row].data.id,
							field_label : records[row].data.name,
							text_detail : records[row].data.detail ,
							listeners: {
		        				deleteMe: function(panel) {
		        					//alert('delete me');
		        					//debugger;
		        					main.remove(panel);
		        				}
		        			}
                		});
                		
                		main.add(obj1);
					}
    				main.doLayout();
                     
                }
        	}
		});
	 	
		
	 	//alert(teams);
		
	},
	initComponent :function(){
		var main = this;
		
		
		this.callParent();
	}
});
 

Ext.define('risks.view.AddRisk', {
    extend: 'Ext.form.Panel',
    alias: 'risk.addRisk',
    fromWin : null,
    fromMain : null,
    level : 0,
    record : null,
    storeRiskSection: risks.listRiskSection,
    forAnonymousUser : function(){
    	this.sendTeam.setVisible(false);//มองไม่เห็น
    	this.deleteRisk.setVisible(false);//มองไม่เห็น
    	this.answer.setVisible(false);//มองไม่เห็น
    	this.editSentResponse.setVisible(false);//มองไม่เห็น	
    },
    loadStore :function(){
    	
    	
    	form = this; 
    	if(sectionid ){
    		risks.listRiskSection.load({
    			params:{ section_id : sectionid },
    			 
         		callback: function(records, o, s) {
                    if (s) {
                    	form.riskSection.setValue(parseInt(sectionid));
                    }
            	}
    		
    		});
    	}
    	else{
    		risks.listRiskSection.load( );
    	}
    	
    	risks.listProgramDetail.load({ params:{ risk_program_group_id : '1' } });
		 
        risks.listRiskLevel.load({ params:{risk_program_group_id : '1' }  });
    	
    	risks.listSectionTeamStore.load();
    	risks.listAcrossTeamStore.load();
    	 
    } ,
    setbuttonShowAns:function(){
    	//this.answer.setVisible(false);//มองไม่เห็น
    	this.answer.setVisible(true);//มองเห็น
    	if(this.record.data.risk_status_id == 5){
			this.answer.setVisible(false);//มองไม่เห็น 
		}
    	 
    },
    setLoadData :function(record){
		form = this;
		this.record = record;
		
		form.getForm().reset();
		//set radio program
		form.riskProgramGroup.forloadData( record.data.risk_program_group_id);
		
		form.getForm().loadRecord(record);
		form.currentRecord = record;
		
			
		
		this.editSentResponse.setVisible(false);//มองไม่เห็น	
		//check level 0 == user then check doc_status == 1 then user can update
		//alert("dddsf " + form.level);	
		
		
		this.textSection.setVisible(false);//มองไม่เห็น section ที่เป็นข้อความ
		this.riskSection.setVisible(true);//มองเห็น list box ของ section
		this.riskSection.allowBlank = false; //ไม่อนุญาติให้ว่าง
		
		this.textProgramGroup.setVisible(false);//มองไม่เห็น section ที่เป็นข้อความ
		this.riskProgramGroup.setVisible(true);//มองเห็น list box ของ section
		
		
		this.textRiskProgramDetail.setVisible(false);//มองเห็นข้อความ
		this.riskProgramDetail.setVisible(true);//มองไม่เห็น list section				 
		this.riskProgramDetail.allowBlank = false;//อนุญาติให้ว่าง
		
		this.textRiskLevel.setVisible(false);//มองเห็นข้อความ
		this.risklevel.setVisible(true);//มองไม่เห็น list section					 
		this.risklevel.allowBlank = false;//อนุญาติให้ว่าง
		
		if(form.level == 0  ){
			 
			if(record.data.risk_status_id == 1){
				this.save.setVisible(true); //มองเห็น
				this.deleteRisk.setVisible(true);//มองเห็น				
			}
			else{				
				this.save.setVisible(false);//มองไม่เห็น
				this.deleteRisk.setVisible(false);//มองไม่เห็น				
			}
			
			if(record.data.risk_status_id >= 3){
				this.textSection.setText("หน่วยงาน :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>" + record.data.risk_section+ "</b></br>",false);
				this.textSection.setVisible(true);//มองเห็นข้อความ
				this.riskSection.setVisible(false);//มองไม่เห็น list section
				this.riskSection.allowBlank = true;//อนุญาติให้ว่าง
				
				
				//this.riskProgramGroup.clinic.boxLabel
				this.textProgramGroup.setText("ประเภท :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>" + record.data.risk_program_group+ "</b></br>",false);
				this.textProgramGroup.setVisible(true);//มองเห็นข้อความ
				this.riskProgramGroup.setVisible(false);
								
				//this.riskProgramDetail.displayTplData[0].name
				this.textRiskProgramDetail.setText("ด้าน/โปรแกรม :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>" + record.data.risk_program_detail + "</b></br>",false);
				this.textRiskProgramDetail.setVisible(true);//มองเห็นข้อความ
				this.riskProgramDetail.setVisible(false);//มองไม่เห็น list section				 
				this.riskProgramDetail.allowBlank = true;//อนุญาติให้ว่าง
				 
				//this.risklevel.displayTplData[0].name
				this.textRiskLevel.setText("ระดับ :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>" +  record.data.level_desc + "</b></br>",false);
				this.textRiskLevel.setVisible(true);//มองเห็นข้อความ
				this.risklevel.setVisible(false);//มองไม่เห็น list section					 
				this.risklevel.allowBlank = true;//อนุญาติให้ว่าง
				
			}
			
		}
		else{
			if(form.level == 1 ){
				if(record.data.risk_status_id >= 3){//เพิ่มทีมที่เกี่ยวข้องเมื่อ ส่งไปแล้วต้องการแก้ไข
					this.editSentResponse.setVisible(true);//มองเห็น	
				}
				else{
					this.editSentResponse.setVisible(false);//มองไม่เห็น			
				}
				if(record.data.risk_status_id < 3){//ส่งทีม
					this.sendTeam.setVisible(true);//มองเห็น	
				} 
				else{
					this.sendTeam.setVisible(false);//มองไม่เห็น			
				}
				if(record.data.risk_status_id > 2){//ปุ่มตอบกลับ 
					this.answer.setVisible(true);//มองเห็น	
				} 
				else{ 
					this.answer.setVisible(false);//มองไม่เห็น			
				}
			}
		}
		
		
		
		//แสดงหน้าเปลี่ยนหน้า 
		if(record.data.risk_status_id >= 3){
			this.responses.getLayout().setActiveItem(1);
			this.responseRisk.setLoadData(record);
			
		}
		else
		{
			this.responses.getLayout().setActiveItem(0);
		}
		
		
	},
    clickRadio: function (ctl,val){
    	 
    	this.main.riskProgramDetail.reset();
    	this.main.risklevel.reset();
		if(ctl.inputValue == "1" && val){
			risks.listProgramDetail.load({
				params:{ risk_program_group_id : ctl.inputValue }
			});
			risks.listRiskLevel.load({
				params:{risk_program_group_id : ctl.inputValue }
			});
		}
		if(ctl.inputValue == "2"&& val){
			risks.listProgramDetail.load({
				params:{ risk_program_group_id : ctl.inputValue }
			});
			risks.listRiskLevel.load({
				params:{risk_program_group_id : ctl.inputValue }
			});
		}
    },
    initComponent: function() {
    	var main = this;
    	main.riskId = Ext.create('risks.gui.RiskId');
    	main.levelId = Ext.create('risks.gui.LevelId',{value: main.level });
    	main.reportDate = Ext.create('risks.gui.reportDate', {anchor : '35%'});
    	main.detailRisk = Ext.create('risks.gui.detailRisk', {anchor : '100% -47' }); 
    	main.solutionRisk = Ext.create('risks.gui.solutionRisk', {anchor : '100% -47' });   
    	
    	 
    	main.risklevel = Ext.create('risks.gui.RiskLevel', {anchor : '100%',store:risks.listRiskLevel});
    	main.riskSection = Ext.create('risks.gui.RiskSection', {anchor : '100%',store:main.storeRiskSection});
    	main.riskProgramDetail = Ext.create('risks.gui.RiskProgramDetail', {anchor : '100%',store:risks.listProgramDetail});
    	main.riskProgramGroup = Ext.create('risks.gui.RiskProgramGroup', {anchor : '100%',
    		clickRadio:main.clickRadio, mainObject:main
    			});
    	
    	
    	main.textSection =Ext.create('risk.gui.TextSection');
    	main.textProgramGroup = Ext.create('risk.gui.TextProgramGroup');
    	main.textRiskProgramDetail = Ext.create('risk.gui.TextRiskProgramDetail');
    	main.textRiskLevel = Ext.create('risk.gui.TextRiskLevel');
    	
    	
    	main.sectionTeam = Ext.create('risks.gui.SectionTeam', {title:'หน่วยงานที่เกี่ยวข้อง',anchor : '100%' ,height:230}); 
    	
    	main.responseRisk = Ext.create('risk.view.ResponseRisk',{anchor : '100%' });
    	
    	main.close = Ext.create('risk.gui.BtClose',{fromWin:main.fromWin });
    	 
    	main.responses  = Ext.create('Ext.panel.Panel',{
			border : false,			 
			anchor: '100%',		 
			layout: 'card',
			activeItem: 0, 
			defaults:{margins:'0 5 5 0'},
			items : [main.sectionTeam,main.responseRisk]
    	});
			
    	
    	
    	
    	main.sendTeam = new Ext.Button({
    		html : '<b>ส่งทีมที่เกี่ยวข้อง</b>',
    		scale   : 'large',
			width : 120,
			listeners : {
				click : function(){
					
					var lenSecTeam =  main.sectionTeam.getLengthSectionTeam();
					var lenCromTeam = main.sectionTeam.getLengthCromTeam();
					
					if(lenSecTeam == 0  &&  lenCromTeam == 0){
						Ext.MessageBox.alert('เตือน', 'กรุณาเลือกทีมที่เกี่ยวข้องด้วย ');
						return ;
					}
					
					main.getForm().submit({
		                url: '/risk/sendTeam',
		                waitMsg: 'Please waiting...',
		                success: function(fp1, o) {
		                	 
		                	Ext.Msg.alert('บันทึก', 'ส่งข้อมูลเสร็จเรียบร้อย.' );
		                	main.getForm().reset();
		                	
		                	if( main.fromWin != null ){
								main.fromWin.hide();
							}
							if(main.fromMain != null){
								main.fromMain.loadDataSearch();
							}  
				       	}
			       }); 
				}
			}
		});
    	
    	main.save = new Ext.Button({
			//text     : 'บันทึก',
    		html : '<b>บันทึก</b>',
			scale   : 'large',
			width : 120,
			listeners: {
		        click: function() {
		        	valid = this.up('form').getForm().isValid();
		        	 
		        	if(valid){ 		        	 
				           main.getForm().submit({
				                url: '/risk/createRisk',
				                waitMsg: 'Please waiting...',
				                success: function(fp1, o) {
				                	 
				                	Ext.Msg.alert('บันทึก', 'บันทึกเสร็จเรียบร้อย.' );
				                	main.getForm().reset();
				                	
				                	//set default combobox section
				                	if(main.level == 0)
				                	{
				                		form.riskSection.setValue(parseInt(sectionid));
				                	}
				                	
				                	if( main.fromWin != null ){
										main.fromWin.hide();
									}
									if(main.fromMain != null){
										main.fromMain.loadDataSearch();
									}	  
						       	}
					       });  
		        	}
		        	else{
		        		alert("ตรวจสอบข้อมูลอีกครั้ง ต้องไม่มีข้อมูลว่าง");
		        	}
			     }  
		       
		    }
					
		});
    	main.editSentResponse = new Ext.Button({
			//text     : 'บันทึก',
    		html : '<b>แก้ไขหน่วยงานที่เกี่ยวข้อง</b>',
			scale   : 'large',
			width : 140,
			cardId : 0,
			
			listeners: {
		        click: function() {
		        	if(this.cardId == 0)
		        	{
		        		main.responses.getLayout().setActiveItem(this.cardId);
		        		this.cardId = this.cardId +1;
		        	}
		        	else
		        	{
		        		if(this.cardId == 1){
			        		main.responses.getLayout().setActiveItem(this.cardId);
			        		this.cardId = this.cardId -1;
			        	}
		        	}
		            
		        //	debugger;
			     }  
		       
		    }
					
		});
    	main.deleteRisk = Ext.create('Ext.Button',{
    		html : '<b>ลบรายการ</b>',
			scale   : 'large',
			width : 120,
			listeners: {
		        click: function() {
		            
		           main.getForm().submit({
		                url: '/risk/deleteRisk',
		                waitMsg: 'Please waiting...',
		                success: function(fp1, o) {
		                	 
		                	Ext.Msg.alert('บันทึก', 'บันทึกเสร็จเรียบร้อย.' );
		                	main.getForm().reset();
		                
		                	if( main.fromWin != null ){
								main.fromWin.hide();
							}
							if(main.fromMain != null){
								main.fromMain.loadDataSearch();
							}	  
				       	}
			       }); 
			     }  
		       
		    }
    	});
    	
    	
    	main.answer = new Ext.Button({
			//text     : 'บันทึก',
    		html : '<b>ตอบกลับ</b>',
			scale   : 'large',
			width : 120,
			//visible :false,
			listeners: {
		        click: function() {
		            
		           main.getForm().submit({
		                url: '/risk/replyRisk',
		                waitMsg: 'Please waiting...',
		                success: function(fp1, o) {
		                	 
		                	Ext.Msg.alert('บันทึก', 'บันทึกเสร็จเรียบร้อย.' );
		               // 	main.getForm().reset();
		                
		                	if( main.fromWin != null ){
								main.fromWin.hide();
							}
							if(main.fromMain != null){
								main.fromMain.loadDataSearch();
							}	  
				       	}
			       }); 
			     }  
		       
		    }
					
		});
    	
    	this.items = [
    	              main.riskId,
    	              main.levelId,
    	              main.reportDate,
    	              main.riskSection,
    	              main.textSection,
    	              
    	              main.riskProgramGroup ,
    	              main.textProgramGroup,
    	              
    	              main.riskProgramDetail,
    	              main.textRiskProgramDetail,
    	              
    	              main.risklevel ,
    	              main.textRiskLevel,
    	              
    	              main.detailRisk,
    	              main.solutionRisk,
    	              main.responses   ,
    	              
    	              ];
    	
    
    	this.dockedItems = [{
            dock: 'bottom',
            xtype: 'toolbar',
            layout : {
				pack : 'center'
			},
			//ui : 'footer',
            items: [
                    	main.editSentResponse,main.deleteRisk,main.sendTeam,main.save,main.answer,main.close
                   ]
        }];
    	
    	this.callParent();
    }
});
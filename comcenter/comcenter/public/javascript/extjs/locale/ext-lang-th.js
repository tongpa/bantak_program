/**
 * List compiled by KillerNay on the extjs.com forums.
 * Thank you KillerNay!
 *
 * Thailand Translations
 */
Ext.onReady(function() {
    var cm = Ext.ClassManager,
        exists = Ext.Function.bind(cm.get, cm);

    if (Ext.Updater) {
        Ext.Updater.defaults.indicatorText = '<div class="loading-indicator">Loading...</div>';
    }

    Ext.define("Ext.locale.th.view.View", {
        override: "Ext.view.View",
        emptyText: ""
    });

    Ext.define("Ext.locale.th.grid.Panel", {
        override: "Ext.grid.Panel",
        ddText: "{0} เลือก แถว {1}"
    });

    Ext.define("Ext.locale.th.TabPanelItem", {
        override: "Ext.TabPanelItem",
        closeText: "»ÔŽá·çº¹Õé"
    });

    Ext.define("Ext.locale.th.form.field.Base", {
        override: "Ext.form.field.Base",
        invalidText: "ค่าในฟิลด์นี้ไม่ถูกต้อง"
    });

    // changing the msg text below will affect the LoadMask
    Ext.define("Ext.locale.th.view.AbstractView", {
        override: "Ext.view.AbstractView",
        msg: "Loading..."
    });

    if (Ext.Date) {
        Ext.Date.monthNames = ["มกราคม","กุมภาพันธ์","มีนาคม","เมษายน","พฤษภาคม","มิถุนายน","กรกฏาคม","สิงหาคม","กันยายน","คุลาคม","พฤศจิกายน","ธันวาคม"];

        Ext.Date.getShortMonthName = function(month) {
            return Ext.Date.monthNames[month].substring(0, 3);
        };

        Ext.Date.monthNumbers = {
            "ม.ค.": 0,
            "ก.พ.": 1,
            "มี.ค.": 2,
            "เม.ย.": 3,
            "พ.ค.": 4,
            "มิ.ย.": 5,
            "ก.ค.": 6,
            "ส.ค.": 7,
            "ก.ย.": 8,
            "ต.ค.": 9,
            "พ.ย.": 10,
            "ธ.ค.": 11
        };

        Ext.Date.getMonthNumber = function(name) {
            return Ext.Date.monthNumbers[name.substring(0, 1).toUpperCase() + name.substring(1, 3).toLowerCase()];
        };

        Ext.Date.dayNames = ["อาทิตย์", "จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์"];

        Ext.Date.getShortDayName = function(day) {
            return Ext.Date.dayNames[day].substring(0, 3);
        };
    }
    if (Ext.MessageBox) {
        Ext.MessageBox.buttonText = {
            ok: "ตกลง",
            cancel: "ยกเลิก",
            yes: "ใช่",
            no: "ไม่ใช่"
        };
    }

    if (exists('Ext.util.Format')) {
        Ext.apply(Ext.util.Format, {
            thousandSeparator: '.',
            decimalSeparator: ',',
            currencySign: '\u0e3f',
            // Thai Baht
            dateFormat: 'm/d/Y'
        });
    }

    Ext.define("Ext.locale.th.picker.Date", {
        override: "Ext.picker.Date",
        todayText: "วันนี้",
        minText: "This date is before the minimum date",
        maxText: "This date is after the maximum date",
        disabledDaysText: "",
        disabledDatesText: "",
        monthNames: Ext.Date.monthNames,
        dayNames: Ext.Date.dayNames,
        nextText: 'เดือนถัดไป (Control+Right)',
        prevText: 'เดือนก่อนหน้า (Control+Left)',
        monthYearText: 'เลือกเดือน (Control+Up/Down to move years)',
        todayTip: "{0} (Spacebar)",
        format: "m/d/y",
        startDay: 0
    });

    Ext.define("Ext.locale.th.picker.Month", {
        override: "Ext.picker.Month",
        okText: "&#160;ตกลง&#160;",
        cancelText: "ยกเลิก"
    });

    Ext.define("Ext.locale.th.toolbar.Paging", {
        override: "Ext.PagingToolbar",
        beforePageText: "หน้า",
        afterPageText: "of {0}",
        firstText: "หน้าแรก",
        prevText: "ก่อนหน้า",
        nextText: "ถัดไป",
        lastText: "หน้าสุดท้าย",
        refreshText: "Refresh",
        displayMsg: "แสดงหน้า {0} - {1} ของ {2}",
        emptyMsg: 'ไม่มีข้อมูล'
    });

    Ext.define("Ext.locale.th.form.field.Text", {
        override: "Ext.form.field.Text",
        minLengthText: "The minimum length for this field is {0}",
        maxLengthText: "The maximum length for this field is {0}",
        blankText: "This field is required",
        regexText: "",
        emptyText: null
    });

    Ext.define("Ext.locale.th.form.field.Number", {
        override: "Ext.form.field.Number",
        minText: "The minimum value for this field is {0}",
        maxText: "The maximum value for this field is {0}",
        nanText: "{0} is not a valid number"
    });

    Ext.define("Ext.locale.th.form.field.Date", {
        override: "Ext.form.field.Date",
        disabledDaysText: "»Disabled",
        disabledDatesText: "»Disabled",
        minText: "The date in this field must be after {0}",
        maxText: "The date in this field must be before {0}",
        invalidText: "{0} is not a valid date - it must be in the format {1}",
        format: "m/d/y",
        altFormats: "m/d/Y|m-d-y|m-d-Y|m/d|m-d|md|mdy|mdY|d|Y-m-d"
    });

    Ext.define("Ext.locale.th.form.field.ComboBox", {
        override: "Ext.form.field.ComboBox",
        valueNotFoundText: undefined
    }, function() {
        Ext.apply(Ext.form.field.ComboBox.prototype.defaultListConfig, {
            loadingText: "Loading..."
        });
    });

    if (exists('Ext.form.field.VTypes')) {
        Ext.apply(Ext.form.field.VTypes, {
            emailText: 'This field should be an e-mail address in the format "user@example.com"',
            urlText: 'This field should be a URL in the format "http:/' + '/www.example.com"',
            alphaText: 'This field should only contain letters and _',
            alphanumText: 'This field should only contain letters, numbers and _'
        });
    }

    Ext.define("Ext.locale.th.form.field.HtmlEditor", {
        override: "Ext.form.field.HtmlEditor",
        createLinkText: 'Please enter the URL for the link:'
    }, function() {
        Ext.apply(Ext.form.field.HtmlEditor.prototype, {
            buttonTips: {
                bold: {
                    title: 'Bold (Ctrl+B)',
                    text: 'Make the selected text bold.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                },
                italic: {
                    title: 'Italic (Ctrl+I)',
                    text: 'Make the selected text italic.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                },
                underline: {
                    title: 'Underline (Ctrl+U)',
                    text: 'Underline the selected text.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                },
                increasefontsize: {
                    title: 'Grow Text',
                    text: 'Increase the font size.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                },
                decreasefontsize: {
                    title: 'Shrink Text',
                    text: 'Decrease the font size.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                },
                backcolor: {
                    title: 'Text Highlight Color',
                    text: 'Change the background color of the selected text.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                },
                forecolor: {
                    title: 'Font Color',
                    text: 'Change the color of the selected text.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                },
                justifyleft: {
                    title: 'Align Text Left',
                    text: 'Align text to the left.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                },
                justifycenter: {
                    title: 'Center Text',
                    text: 'Center text in the editor.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                },
                justifyright: {
                    title: 'Align Text Right',
                    text: 'Align text to the right.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                },
                insertunorderedlist: {
                    title: 'Bullet List',
                    text: 'Start a bulleted list.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                },
                insertorderedlist: {
                    title: 'Numbered List',
                    text: 'Start a numbered list.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                },
                createlink: {
                    title: 'Hyperlink',
                    text: 'Make the selected text a hyperlink.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                },
                sourceedit: {
                    title: 'Source Edit',
                    text: 'Switch to source editing mode.',
                    cls: Ext.baseCSSPrefix + 'html-editor-tip'
                }
            }
        });
    });

    Ext.define("Ext.locale.th.grid.header.Container", {
        override: "Ext.grid.header.Container",
        sortAscText: "Sort Ascending",
        sortDescText: "Sort Descending",
        lockText: "Lock Column",
        unlockText: "Unlock Column",
        columnsText: "Columns"
    });

    Ext.define("Ext.locale.th.grid.GroupingFeature", {
        override: "Ext.grid.GroupingFeature",
        emptyGroupText: '(None)',
        groupByText: 'Group By This Field',
        showGroupsText: 'Show in Groups'
    });

    Ext.define("Ext.locale.th.grid.PropertyColumnModel", {
        override: "Ext.grid.PropertyColumnModel",
        nameText: "Name",
        valueText: "Value",
        dateFormat: "m/j/Y"
    });

});

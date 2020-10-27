#############################################################################
# Generated by PAGE version 5.5
#  in conjunction with Tcl version 8.6
#  Oct 27, 2020 12:52:34 PM CET  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background #000000 
    wm focusmodel $top passive
    wm geometry $top 934x637+399+186
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "PureNEPage" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra45 \
        -borderwidth 2 -background #000000 -height 85 -width 916 
    vTcl:DefineAlias "$top.fra45" "titleFrame" vTcl:WidgetProc "PureNEPage" 1
    set site_3_0 $top.fra45
    label $site_3_0.lab46 \
        -background #000000 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #fff -text {Pure Nash Equilibria } 
    vTcl:DefineAlias "$site_3_0.lab46" "titleLabel" vTcl:WidgetProc "PureNEPage" 1
    place $site_3_0.lab46 \
        -in $site_3_0 -x 0 -relx 0.284 -y 0 -rely 0.238 -width 0 \
        -relwidth 0.44 -height 0 -relheight 0.429 -anchor nw \
        -bordermode ignore 
    frame $top.fra47 \
        -borderwidth 2 -background #000 -height 497 -width 909 
    vTcl:DefineAlias "$top.fra47" "mainFrame" vTcl:WidgetProc "PureNEPage" 1
    set site_3_0 $top.fra47
    frame $site_3_0.fra58 \
        -borderwidth 2 -background #000 -height 286 -width 551 
    vTcl:DefineAlias "$site_3_0.fra58" "payoffMatrixFrame" vTcl:WidgetProc "PureNEPage" 1
    set site_4_0 $site_3_0.fra58
    frame $site_4_0.fra59 \
        -borderwidth 2 -relief groove -background #000 -height 101 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 173 
    vTcl:DefineAlias "$site_4_0.fra59" "payoffFrame_1" vTcl:WidgetProc "PureNEPage" 1
    set site_5_0 $site_4_0.fra59
    entry $site_5_0.ent49 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 44 
    vTcl:DefineAlias "$site_5_0.ent49" "payoffEntryL00" vTcl:WidgetProc "PureNEPage" 1
    entry $site_5_0.ent50 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 44 
    vTcl:DefineAlias "$site_5_0.ent50" "payoffEntryR00" vTcl:WidgetProc "PureNEPage" 1
    label $site_5_0.lab51 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text ( 
    vTcl:DefineAlias "$site_5_0.lab51" "Label1_3" vTcl:WidgetProc "PureNEPage" 1
    label $site_5_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text ) 
    vTcl:DefineAlias "$site_5_0.lab52" "Label1_1_1" vTcl:WidgetProc "PureNEPage" 1
    label $site_5_0.lab53 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text , 
    vTcl:DefineAlias "$site_5_0.lab53" "Label1_2_1" vTcl:WidgetProc "PureNEPage" 1
    place $site_5_0.ent49 \
        -in $site_5_0 -x 0 -relx 0.162 -y 0 -rely 0.316 -width 44 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.ent50 \
        -in $site_5_0 -x 0 -relx 0.595 -y 0 -rely 0.316 -width 44 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.lab51 \
        -in $site_5_0 -x 0 -relx 0.051 -y 0 -rely 0.211 -width 0 \
        -relwidth 0.074 -height 0 -relheight 0.379 -anchor nw \
        -bordermode ignore 
    place $site_5_0.lab52 \
        -in $site_5_0 -x 0 -relx 0.869 -y 0 -rely 0.211 -width 0 \
        -relwidth 0.074 -height 0 -relheight 0.379 -anchor nw \
        -bordermode ignore 
    place $site_5_0.lab53 \
        -in $site_5_0 -x 0 -relx 0.434 -y 0 -rely 0.105 -width 0 \
        -relwidth 0.126 -height 0 -relheight 0.589 -anchor nw \
        -bordermode ignore 
    frame $site_4_0.fra60 \
        -borderwidth 2 -relief groove -background #000 -height 101 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 173 
    vTcl:DefineAlias "$site_4_0.fra60" "payoffFrame_1_1" vTcl:WidgetProc "PureNEPage" 1
    set site_5_0 $site_4_0.fra60
    entry $site_5_0.ent49 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 44 
    vTcl:DefineAlias "$site_5_0.ent49" "payoffEntryL01" vTcl:WidgetProc "PureNEPage" 1
    entry $site_5_0.ent50 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 44 
    vTcl:DefineAlias "$site_5_0.ent50" "payoffEntryR01" vTcl:WidgetProc "PureNEPage" 1
    label $site_5_0.lab51 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text ( 
    vTcl:DefineAlias "$site_5_0.lab51" "Label1_3_1" vTcl:WidgetProc "PureNEPage" 1
    label $site_5_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text ) 
    vTcl:DefineAlias "$site_5_0.lab52" "Label1_1_1_1" vTcl:WidgetProc "PureNEPage" 1
    label $site_5_0.lab53 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text , 
    vTcl:DefineAlias "$site_5_0.lab53" "Label1_2_1_1" vTcl:WidgetProc "PureNEPage" 1
    frame $site_5_0.fra61 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 101 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 173 
    vTcl:DefineAlias "$site_5_0.fra61" "payoffFrame_1_2" vTcl:WidgetProc "PureNEPage" 1
    set site_6_0 $site_5_0.fra61
    entry $site_6_0.ent49 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 44 
    vTcl:DefineAlias "$site_6_0.ent49" "payoffEntry00_1_2" vTcl:WidgetProc "PureNEPage" 1
    entry $site_6_0.ent50 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 44 
    vTcl:DefineAlias "$site_6_0.ent50" "payoffEntry01_1_2" vTcl:WidgetProc "PureNEPage" 1
    label $site_6_0.lab51 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text ( 
    vTcl:DefineAlias "$site_6_0.lab51" "Label1_3_2" vTcl:WidgetProc "PureNEPage" 1
    label $site_6_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text ) 
    vTcl:DefineAlias "$site_6_0.lab52" "Label1_1_1_2" vTcl:WidgetProc "PureNEPage" 1
    label $site_6_0.lab53 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text , 
    vTcl:DefineAlias "$site_6_0.lab53" "Label1_2_1_2" vTcl:WidgetProc "PureNEPage" 1
    place $site_6_0.ent49 \
        -in $site_6_0 -x 0 -relx 0.162 -y 0 -rely 0.316 -width 44 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.ent50 \
        -in $site_6_0 -x 0 -relx 0.595 -y 0 -rely 0.316 -width 44 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_6_0.lab51 \
        -in $site_6_0 -x 0 -relx 0.051 -y 0 -rely 0.211 -width 0 \
        -relwidth 0.074 -height 0 -relheight 0.379 -anchor nw \
        -bordermode ignore 
    place $site_6_0.lab52 \
        -in $site_6_0 -x 0 -relx 0.869 -y 0 -rely 0.211 -width 0 \
        -relwidth 0.074 -height 0 -relheight 0.379 -anchor nw \
        -bordermode ignore 
    place $site_6_0.lab53 \
        -in $site_6_0 -x 0 -relx 0.434 -y 0 -rely 0.105 -width 0 \
        -relwidth 0.126 -height 0 -relheight 0.589 -anchor nw \
        -bordermode ignore 
    place $site_5_0.ent49 \
        -in $site_5_0 -x 0 -relx 0.162 -y 0 -rely 0.316 -width 44 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.ent50 \
        -in $site_5_0 -x 0 -relx 0.595 -y 0 -rely 0.316 -width 44 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.lab51 \
        -in $site_5_0 -x 0 -relx 0.051 -y 0 -rely 0.211 -width 0 \
        -relwidth 0.074 -height 0 -relheight 0.379 -anchor nw \
        -bordermode ignore 
    place $site_5_0.lab52 \
        -in $site_5_0 -x 0 -relx 0.869 -y 0 -rely 0.211 -width 0 \
        -relwidth 0.074 -height 0 -relheight 0.379 -anchor nw \
        -bordermode ignore 
    place $site_5_0.lab53 \
        -in $site_5_0 -x 0 -relx 0.434 -y 0 -rely 0.105 -width 0 \
        -relwidth 0.126 -height 0 -relheight 0.589 -anchor nw \
        -bordermode ignore 
    place $site_5_0.fra61 \
        -in $site_5_0 -x 0 -relx 0.495 -y 0 -rely 1.856 -width 0 -relwidth 1 \
        -height 0 -relheight 1 -anchor nw -bordermode ignore 
    frame $site_4_0.fra63 \
        -borderwidth 2 -relief groove -background #000 -height 101 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 173 
    vTcl:DefineAlias "$site_4_0.fra63" "payoffFrame_1_4" vTcl:WidgetProc "PureNEPage" 1
    set site_5_0 $site_4_0.fra63
    entry $site_5_0.ent49 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 44 
    vTcl:DefineAlias "$site_5_0.ent49" "payoffEntryL11" vTcl:WidgetProc "PureNEPage" 1
    entry $site_5_0.ent50 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 44 
    vTcl:DefineAlias "$site_5_0.ent50" "payoffEntryR11" vTcl:WidgetProc "PureNEPage" 1
    label $site_5_0.lab51 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text ( 
    vTcl:DefineAlias "$site_5_0.lab51" "Label1_3_4" vTcl:WidgetProc "PureNEPage" 1
    label $site_5_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text ) 
    vTcl:DefineAlias "$site_5_0.lab52" "Label1_1_1_4" vTcl:WidgetProc "PureNEPage" 1
    label $site_5_0.lab53 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text , 
    vTcl:DefineAlias "$site_5_0.lab53" "Label1_2_1_4" vTcl:WidgetProc "PureNEPage" 1
    place $site_5_0.ent49 \
        -in $site_5_0 -x 0 -relx 0.162 -y 0 -rely 0.316 -width 44 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.ent50 \
        -in $site_5_0 -x 0 -relx 0.595 -y 0 -rely 0.316 -width 44 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.lab51 \
        -in $site_5_0 -x 0 -relx 0.051 -y 0 -rely 0.211 -width 0 \
        -relwidth 0.074 -height 0 -relheight 0.379 -anchor nw \
        -bordermode ignore 
    place $site_5_0.lab52 \
        -in $site_5_0 -x 0 -relx 0.869 -y 0 -rely 0.211 -width 0 \
        -relwidth 0.074 -height 0 -relheight 0.379 -anchor nw \
        -bordermode ignore 
    place $site_5_0.lab53 \
        -in $site_5_0 -x 0 -relx 0.434 -y 0 -rely 0.105 -width 0 \
        -relwidth 0.126 -height 0 -relheight 0.589 -anchor nw \
        -bordermode ignore 
    frame $site_4_0.fra64 \
        -borderwidth 2 -relief groove -background #000 -height 101 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 173 
    vTcl:DefineAlias "$site_4_0.fra64" "payoffFrame_1_3" vTcl:WidgetProc "PureNEPage" 1
    set site_5_0 $site_4_0.fra64
    entry $site_5_0.ent49 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 44 
    vTcl:DefineAlias "$site_5_0.ent49" "payoffEntryL10" vTcl:WidgetProc "PureNEPage" 1
    entry $site_5_0.ent50 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 44 
    vTcl:DefineAlias "$site_5_0.ent50" "payoffEntryR10" vTcl:WidgetProc "PureNEPage" 1
    label $site_5_0.lab51 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text ( 
    vTcl:DefineAlias "$site_5_0.lab51" "Label1_3_3" vTcl:WidgetProc "PureNEPage" 1
    label $site_5_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text ) 
    vTcl:DefineAlias "$site_5_0.lab52" "Label1_1_1_3" vTcl:WidgetProc "PureNEPage" 1
    label $site_5_0.lab53 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #fff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text , 
    vTcl:DefineAlias "$site_5_0.lab53" "Label1_2_1_3" vTcl:WidgetProc "PureNEPage" 1
    place $site_5_0.ent49 \
        -in $site_5_0 -x 0 -relx 0.162 -y 0 -rely 0.316 -width 44 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.ent50 \
        -in $site_5_0 -x 0 -relx 0.595 -y 0 -rely 0.316 -width 44 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.lab51 \
        -in $site_5_0 -x 0 -relx 0.051 -y 0 -rely 0.211 -width 0 \
        -relwidth 0.074 -height 0 -relheight 0.379 -anchor nw \
        -bordermode ignore 
    place $site_5_0.lab52 \
        -in $site_5_0 -x 0 -relx 0.869 -y 0 -rely 0.211 -width 0 \
        -relwidth 0.074 -height 0 -relheight 0.379 -anchor nw \
        -bordermode ignore 
    place $site_5_0.lab53 \
        -in $site_5_0 -x 0 -relx 0.434 -y 0 -rely 0.105 -width 0 \
        -relwidth 0.126 -height 0 -relheight 0.589 -anchor nw \
        -bordermode ignore 
    place $site_4_0.fra59 \
        -in $site_4_0 -x 0 -relx 0.055 -y 0 -rely 0.087 -width 0 \
        -relwidth 0.417 -height 0 -relheight 0.33 -anchor nw \
        -bordermode ignore 
    place $site_4_0.fra60 \
        -in $site_4_0 -x 0 -relx 0.477 -y 0 -rely 0.087 -width 0 \
        -relwidth 0.417 -height 0 -relheight 0.33 -anchor nw \
        -bordermode ignore 
    place $site_4_0.fra63 \
        -in $site_4_0 -x 0 -relx 0.477 -y 0 -rely 0.435 -width 0 \
        -relwidth 0.417 -height 0 -relheight 0.33 -anchor nw \
        -bordermode ignore 
    place $site_4_0.fra64 \
        -in $site_4_0 -x 0 -relx 0.055 -y 0 -rely 0.435 -width 0 \
        -relwidth 0.417 -height 0 -relheight 0.33 -anchor nw \
        -bordermode ignore 
    label $site_3_0.lab68 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #1efff3 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text A 
    vTcl:DefineAlias "$site_3_0.lab68" "Label1_2" vTcl:WidgetProc "PureNEPage" 1
    label $site_3_0.lab69 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #1efff3 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text B 
    vTcl:DefineAlias "$site_3_0.lab69" "Label1_2_2" vTcl:WidgetProc "PureNEPage" 1
    label $site_3_0.lab71 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #ff3136 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text C 
    vTcl:DefineAlias "$site_3_0.lab71" "Label1_2_3" vTcl:WidgetProc "PureNEPage" 1
    label $site_3_0.lab72 \
        -activebackground #f9f9f9 -activeforeground black -background #000 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #ff3136 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text D 
    vTcl:DefineAlias "$site_3_0.lab72" "Label1_2_4" vTcl:WidgetProc "PureNEPage" 1
    label $site_3_0.lab73 \
        -background #000 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 20 -weight bold} \
        -foreground #ff3136 -text {Player II} 
    vTcl:DefineAlias "$site_3_0.lab73" "Label1" vTcl:WidgetProc "PureNEPage" 1
    button $site_3_0.but88 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #000 -disabledforeground #a3a3a3 \
        -font {-family {MV Boli} -size 22 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #61ff33 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -relief groove -text Solve 
    vTcl:DefineAlias "$site_3_0.but88" "Button1" vTcl:WidgetProc "PureNEPage" 1
    place $site_3_0.fra58 \
        -in $site_3_0 -x 0 -relx 0.11 -y 0 -rely 0.342 -width 0 \
        -relwidth 0.606 -height 0 -relheight 0.575 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab68 \
        -in $site_3_0 -x 0 -relx 0.011 -y 0 -rely 0.423 -width 0 \
        -relwidth 0.09 -height 0 -relheight 0.093 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab69 \
        -in $site_3_0 -x 0 -relx 0.011 -y 0 -rely 0.624 -width 0 \
        -relwidth 0.09 -height 0 -relheight 0.093 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab71 \
        -in $site_3_0 -x 0 -relx 0.22 -y 0 -rely 0.221 -width 0 \
        -relwidth 0.09 -height 0 -relheight 0.093 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab72 \
        -in $site_3_0 -x 0 -relx 0.473 -y 0 -rely 0.221 -width 0 \
        -relwidth 0.09 -height 0 -relheight 0.093 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab73 \
        -in $site_3_0 -x 0 -relx 0.297 -y 0 -rely 0.06 -width 0 \
        -relwidth 0.178 -height 0 -relheight 0.113 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but88 \
        -in $site_3_0 -x 0 -relx 0.737 -y 0 -rely 0.543 -width 136 \
        -relwidth 0 -height 63 -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra45 \
        -in $top -x 0 -relx 0.041 -y 0 -rely 0.029 -width 0 -relwidth 0.928 \
        -height 0 -relheight 0.124 -anchor nw -bordermode ignore 
    place $top.fra47 \
        -in $top -x 0 -relx 0.041 -y 0 -rely 0.176 -width 0 -relwidth 0.921 \
        -height 0 -relheight 0.728 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

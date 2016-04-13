from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget

mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "space",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "Return", lazy.spawn("urxvt")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.nextlayout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
]

groups = [Group(i) for i in "asdfuiop"]

for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )

fonts = {'font': 'Envy Code R', 'fontsize': 10}
fontcolors = fonts.copy()

borders = {
    'border_normal': '#ffffff',
    'border_focus': '#FFBF00',
    'border_width': 2,
    'margin': 1,
}

layouts = [
    layout.Tile(ratio=0.33, **borders),
    layout.Max(),
    layout.RatioTile(**borders),
    layout.MonadTall(**borders),
    layout.Stack(num_stacks=2, **borders),
    layout.TreeTab(active_bg="#A59461", active_fg="#000000", inactive_bg="#000000", sections=['Files'], **fontcolors),
#    layout.Float(),
]

widget_defaults = dict(
    font='Envy CodeR',
    fontsize=12,
    padding=2,
)

screens = [
    Screen(
        top=bar.Bar(
            [
		widget.TextBox(text="|"),
                widget.GroupBox(),
                #widget.Prompt(),
		widget.TextBox(text="| Layout:"),
		widget.CurrentLayout(),
		#
		#widget.TaskList(),
		widget.Spacer(),
                widget.Systray(),
                widget.Clock(format='%I:%M %p  %a %b %d, %Y'),
		widget.TextBox(text=" Vol."),
		widget.Volume(),
		widget.TextBox(text=" Bat."),
		widget.Battery(battery_name="BAT1"),
            ],
            22,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# Automatically float these types:
floating_layout = layout.Floating(auto_float_types=[
    "notification",
    "toolbar",
    "splash",
    "dialog",
    "utility",
])

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = False
wmname = "qtile"

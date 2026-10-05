# Ill try to use as little AI as Possible but Sometimes my skills arent good enought.
# But everything ill Code with AI will get Noted in Obsidian. You Can find my Notes for this Project in the Reposetory
# Thx for using this Programm. If you have some Correction for my code feel free to Edit and commit you Changes.

import os
from textual.binding import Binding
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static, Button, Label, TabbedContent, TabPane, RadioButton, RadioSet, Tabs, Select, Input, SelectionList, LoadingIndicator
from textual.containers import Container, Center, Vertical, Horizontal
from textual.screen import Screen
from textual.theme import Theme
import subprocess, re
from textual_autocomplete import AutoComplete

LOGO = """       


[#F85552]         .8.          [/#F85552][#DFA000] 8 888888888o   [/#DFA000][#8DA101]8 888888888o   [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888888888  [/#DF69BA]           [#35A77C]8 888888888o  [/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 8888888888   [/#F85552][#DFA000]8 8888888888   [/#DFA000]
[#F85552]        .888.         [/#F85552][#DFA000] 8 8888    `88. [/#DFA000][#8DA101]8 8888    `88. [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 8888    `88.[/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552]       :88888.        [/#F85552][#DFA000] 8 8888     `88 [/#DFA000][#8DA101]8 8888     `88 [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 8888     `88[/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552]      . `88888.       [/#F85552][#DFA000] 8 8888     ,88 [/#DFA000][#8DA101]8 8888     ,88 [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 8888     ,88[/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552]     .8. `88888.      [/#F85552][#DFA000] 8 8888.   ,88' [/#DFA000][#8DA101]8 8888.   ,88' [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 888888888888[/#DF69BA]           [#35A77C]8 8888.   ,88'[/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 888888888888 [/#F85552][#DFA000]8 888888888888 [/#DFA000]
[#F85552]    .8`8. `88888.     [/#F85552][#DFA000] 8 888888888P'  [/#DFA000][#8DA101]8 888888888P'  [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 888888888P' [/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552]   .8' `8. `88888.    [/#F85552][#DFA000] 8 8888         [/#DFA000][#8DA101]8 8888         [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 8888        [/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552]  .8'   `8. `88888.   [/#F85552][#DFA000] 8 8888         [/#DFA000][#8DA101]8 8888         [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 8888        [/#35A77C][#F57D26] ` 8888     ,8P[/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552] .888888888. `88888.  [/#F85552][#DFA000] 8 8888         [/#DFA000][#8DA101]8 8888         [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 8888        [/#35A77C][#F57D26]   8888   ,d8P [/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552].8'       `8. `88888. [/#F85552][#DFA000] 8 8888         [/#DFA000][#8DA101]8 8888         [/#8DA101][#3A94C5] 8 888888888888 [/#3A94C5][#DF69BA]8 888888888888[/#DF69BA]           [#35A77C]8 8888        [/#35A77C][#F57D26]    `Y88888P'  [/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]

"""
my_theme = Theme(
    name="my-theme",
    primary="#93B259",
    )

class Logo(Label):                                 #AI (Noted how it Works in the Obsidian Vault)
    def __init__(self) -> None:                    #AI
        super().__init__(LOGO, classes="title")    #AI

def GetKeyboardLayouts():
    output = subprocess.check_output(["localectl", "list-keymaps"], text=True)
    return output.splitlines()

def GetTimeZone():
    output = subprocess.check_output(["timedatectl", "list-timezones"], text=True)
    return output.splitlines()

def GetNetworkInterfaces():
    out = subprocess.run("ls /sys/class/net | grep -E '^(en|wl)'", shell=True, capture_output=True, text=True) #AI
    interfaces = out.stdout.split()
    return interfaces

# The First Screen you will See when you Launch the TUI
class StartScreen(Screen):
    def compose(self):
        yield Logo()
        with Container(id="button1area"):          #AI Told me Abaut Containers while Debuging (Noted how it Works in the Obsidian Vault)
            yield Button("Start",classes="button1", id="Start")
            yield Button("Exit",classes="button1", id="Exit")
    def on_button_pressed(self, event: Button.Pressed) -> None: #AI Helped me how Buttons Work and told me hwo to switch screens
        if event.button.id == "Start":                          #(Noted how it Works in the Obsidian Vault)
            self.app.push_screen(SeconndScreen())               #
        if event.button.id == "Exit":                           #
            self.app.exit()                                     #

# The Screen you will se after the Start Screen. Its here for the Selections of the Options for the Installer
class SeconndScreen(Screen):
    # Variables for Summary Screen
    selected_TimeZone = "[#F85552] Please Select Timezone [/#F85552]"
    
    selected_layout = "[#F85552] Please Select Keyboard Layout [/#F85552]"
    
    Needed_To_Start ={
        "Layout_Selected": False,
        "TimeZone_Selected": False,
        "User_Password_Matches": False,
        "Root_Password_Matches": False,
        "Hostname_Selected": False,
        "Username_Selected": False,
        "Internet_Connected": False
    }
    Selected_disk: str | None = None
    # Variables for Functions
    selected_ssid: str | None = None
    selected_interface: str | None = None
    entered_password: str | None = None
    selected_PartitionTable: str | None = None
    selected_Username: str | None = None
    selected_UserPassword: str | None = None
    selected_UserPassword2: str | None = None
    selected_RootPassword: str | None = None
    selected_RootPassword2: str | None = None
    selected_Hostname: str | None = None
    selected_Software: str | None = None
    selected_Software_Array = []
    BINDINGS = [                                                #AI Helped me with the Bindings (Noted how it Works in the Obsidian Vault)
        Binding("left", "prev_tab", "Previous step"),           #
        Binding("right", "next_tab", "Next step"),              #
        Binding("up", "focus_previous", "Focus previous"),      #
        Binding("down", "focus_next", "Focus next"),            #
    ]
    def compose(self):
        yield Logo()
        with TabbedContent(classes="Installation"):
            with TabPane("Locale", classes="InstallationTabs"):
                with Container(id="button2area"):
                     layout_input = Input(placeholder="Search keyboard layout...", id="KeyboardLayoutInput",classes="select1")  #AI
                     yield layout_input                                                                                         #
                     yield AutoComplete(layout_input, candidates=GetKeyboardLayouts())                                          #
                     TimeZone_input = Input(placeholder="Search Time Zone...", id="TimeZoneInput", classes="select1")           #
                     yield TimeZone_input                                                                                       #
                     yield AutoComplete(TimeZone_input, candidates=GetTimeZone())                                               #

            with TabPane("Device Selection", classes="InstallationTabs"):
                with Container(id="button2area"):
                    yield Label("[#5c6a72]On Which Devive do you want to Install Apple Puff?[/#5c6a72]",classes="DevSecText DevSec")
                    yield Label("[#F85552]!THE WHOLE DEVICE WILL BE EREASED![/#F85552]",classes="DevSecText DevSec")
                    diskoutput = subprocess.check_output(           #AI corrected my Idea (Noted how it Works in the Obsidian Vault)
                        ["lsblk", "-dn", "-o", "NAME,MODEL,SIZE"],  #
                        text=True                                   #
                    )                                               #
                    Disks = diskoutput.splitlines()                 #
                    with Center():                                  # Ai Told me about Center (Noted how it Works in the Obsidian Vault)
                        with RadioSet(classes="RadioSetDisk", id="SelectDisk"):
                            for disk in Disks:
                                yield RadioButton(disk)
                        yield Select.from_values(["GPT", "MBR"], value="GPT", allow_blank=False, id="PartitionTable", classes="select1")

            with TabPane("Machine Stuff", classes="InstallationTabs"):
                with Container(id="button2area"):        
                    yield Input(placeholder="Enter Hostname", id="EnterHostname", classes="select1")
                    yield Static(id="RootPassswordError")
                    yield Input(placeholder="Enter Root Password", id="EnterRootPassword", password=True, classes="select1")
                    yield Input(placeholder="Enter Toor Password Again", id="EnterRootPassword2", password=True, classes="select1")
                    yield Button("Check", id="CheckRoot", classes="button1")

            with TabPane("User Creation", classes="InstallationTabs"):
                with Container(id="button2area"):
                    yield Input(placeholder="Enter Username", id="EnterUsername", classes="select1")
                    yield Static(id="UserPassswordError")
                    yield Input(placeholder="Enter Password", id="EnterUserPassword", password=True, classes="select1")
                    yield Input(placeholder="Enter Password Again", id="EnterUserPassword2", password=True, classes="select1")
                    yield Button("Check", id="CheckUser", classes="button1")
                    
            with TabPane("Network Connection", classes="InstallationTabs"):
                with Container(id="button2area"):
                    NetworkInterfaces = GetNetworkInterfaces()
                    yield Select(((NetInt, NetInt)for NetInt in NetworkInterfaces), id="SelectNetworkInterface", classes="select1") #AI
                    yield Select(options=[], id="SSID-Select", classes="select1")
                    yield Input(placeholder="Enter Password", id="EnterWLANPassword", password=True)
                    yield Static(id="ConnectionStatus")
                    yield Button("Connect", id="ConnectWLANButton", classes="button1")

            with TabPane("Software", classes="InstallationTabs"):
                with Container(id="button2area"):
                    yield SelectionList(
                        ("Firefox", "firefox", True),
                        ("Obsidian", "obsidian"),
                        ("NeoVim", "neovim", True),
                        ("LibreOffice", "libreoffice-fresh"),
                        ("Btop", "btop", True),
                        ("cmus (Terminal Audio Player)", "cmus", True),
                        ("tlp (Laptop Power Optimization)", "tlp"),
                        id="select_software",)
                    
            with TabPane("Summary", classes="InstallationTabs"):
                with Container(id="button2area"):
                    yield Static(classes="SummaryLabel", id="SummaryLabel")
                    yield Button("Start Install", classes="button1", id="StartPostInstallScreen")

    @property   #AI
    def Summary(self) -> str:
        not_set = lambda text: f"[#F85552] Please Select {text} [/#F85552]"
        return (
            f"Timezone: {self.selected_TimeZone}\n"
            f"Selected Keyboard Layout: {self.selected_layout}\n"
            f"Selected Disk to install Apple Puff on: {self.Selected_disk or not_set('Disk')}\n"
            f"Internet Connected: {self.Needed_To_Start['Internet_Connected']}\n"
        )

    @on(Input.Changed, "#TimeZoneInput")                            #AI
    def on_TimeZone_changed(self, event: Input.Changed) -> None:      #
        self.selected_TimeZone = event.value
        SummaryScreen = self.query_one("#SummaryLabel", Static)
        SummaryScreen.update(self.Summary)
        subprocess.run(["timedatectl", "set-timezone", event.value])
        self.Needed_To_Start["TimeZone_Selected"] = True

    @on(Input.Changed, "#KeyboardLayoutInput")                      #AI
    def on_layout_changed(self, event: Input.Changed) -> None:      #
        self.selected_layout = event.value                          #
        SummaryScreen = self.query_one("#SummaryLabel", Static)
        SummaryScreen.update(self.Summary)     
        subprocess.run(["loadkeys", event.value])
        self.Needed_To_Start["Layout_Selected"] = True

    @on(RadioButton.Changed, "#SelectDisk")
    def on_disk_changed(self, event: RadioButton.Changed) -> None:
        #self.Selected_disk = event.value
        self.Selected_disk = str(event.pressed.label).split()[0]        #AI
        self.query_one("#SummaryLabel", Static).update(self.Summary)    #AI
        #SummaryScreen = self.query_one("#SummaryLabel", Static)
        #SummaryScreen.update(self.Summary) 

    @on(Select.Changed, "#PartitionTable")
    def on_Partition_Table_changed(self, event: Select.Changed) -> None:
        self.selected_PartitionTable = event.value

    @on(Input.Changed, "#EnterUsername")
    def on_username_changed(self, event: Input.Changed) -> None:
        self.selected_Username = event.value.lower()
        self.Needed_To_Start["Username_Selected"] = bool(event.value.strip()) #AI

    @on(Input.Changed, "#EnterUserPassword")
    def on_user_password_changed(self, event: Input.Changed) -> None:
        self.selected_UserPassword = event.value

    @on(Input.Changed, "#EnterUserPassword2")
    def on_user_password_changed2(self, event: Input.Changed) -> None:
        self.selected_UserPassword2 = event.value

    @on(Input.Changed, "#EnterRootPassword")
    def on_root_password_changed(self, event: Input.Changed) -> None:
        self.selected_RootPassword = event.value

    @on(Input.Changed, "#EnterRootPassword2")
    def on_root_password_changed2(self, event: Input.Changed) -> None:
        self.selected_RootPassword2 = event.value
    
    @on(Button.Pressed, "#CheckUser")
    def on_Check_User_Pressed(self, event:Button.Pressed) -> None:
        error = self.query_one("#UserPassswordError", Static)
        if not self.selected_UserPassword or self.selected_UserPassword != self.selected_UserPassword2: #AI          
            error.update("[#F85552]Passwords do not Match[/#F85552]")
            error.styles.display = "block"
            self.Needed_To_Start["User_Password_Matches"] = False
        else:
            error.styles.display = "none"
            self.Needed_To_Start["User_Password_Matches"] = True

    @on(Button.Pressed, "#CheckRoot")
    def on_Check_Root_Pressed(self, event:Button.Pressed) -> None:
        error = self.query_one("#RootPassswordError", Static)
        if not self.selected_RootPassword or self.selected_RootPassword != self.selected_RootPassword2:     #AI     
            error.update("[#F85552]Passwords do not Match[/#F85552]")
            error.styles.display = "block"
            self.Needed_To_Start["Root_Password_Matches"] = False
        else:
            error.styles.display = "none"
            self.Needed_To_Start["Root_Password_Matches"] = True

    @on(Input.Changed, "#EnterHostname")
    def on_Hostname_Changed(self, event: Input.Changed) -> None:
        self.selected_Hostname = event.value
        self.Needed_To_Start["Hostname_Selected"] = True

    @on(Select.Changed, "#SelectNetworkInterface")
    def on_network_interface_selected(self, event: Select.Changed) -> None:
        SSID_select = self.query_one("#SSID-Select", Select)               #AI
        Password_Input = self.query_one("#EnterWLANPassword", Input)
        Connect_Button = self.query_one("#ConnectWLANButton", Button)
        ConnectionStatus = self.query_one("#ConnectionStatus", Static)
        SummaryScreen = self.query_one("#SummaryLabel", Static)
        if event.value == Select.NULL:
            SSID_select.styles.display = "none"     #AI
            Password_Input.styles.display = "none"
            Connect_Button.styles.display = "none"  
            ConnectionStatus.styles.display = "none"
            return
        
        if "wl" in event.value:
            try:
                self.selected_interface = event.value
             
                subprocess.run(
                ["iwctl", "station", event.value, "scan"]
                )
                output = subprocess.check_output(
                    ["sh", "-c", r"""iwctl station "$1" get-networks | sed 's/\x1b\[[0-9;]*m//g' | tail -n +5 | sed 's/^[ >]*//; s/ \{2,\}.*//' | grep -v '^$'""", "sh", event.value],  #AI
                    text=True,
                )
                new_options = [line for line in output.splitlines() if line.strip()] #AI

                SSID_select.set_options((s, s) for s in new_options)  #AI
                SSID_select.clear()                                     #AI
                SSID_select.styles.display = "block"                  #AI
                Password_Input.clear()   
                Password_Input.styles.display = "block"
                Connect_Button.styles.display = "block"
                self.Needed_To_Start["Internet_Connected"] = True
            except subprocess.CalledProcessError as Error:
                ConnectionStatus.update(Error())
                ConnectionStatus.styles.color = "#F85552"
                ConnectionStatus.styles.display = "block"
            
        elif "en" in event.value:
            ConnectionStatus.styles.display = "none"        #AI
            command = "/sys/class/net/" + event.value + "/operstate"
            LANOUT = subprocess.check_output(
            ["cat", command],
            text=True,
            ).strip()
            if LANOUT == "up":
                ConnectionStatus.update("Internet Connected")
                ConnectionStatus.styles.color = "#8DA101"
                self.Needed_To_Start["Internet_Connected"] = True
            else:
                ConnectionStatus.update("Connection Failed:")
                ConnectionStatus.styles.color = "#F85552"
            ConnectionStatus.styles.display = "block"
        else:
            ConnectionStatus = self.query_one("#ConnectionStatus", Static)
            ConnectionStatus.update("Something Went Wrong, Please Select an WLAN or LAN interface")
            ConnectionStatus.styles.color = "#F85552"
            ConnectionStatus.styles.display = "block"
        SummaryScreen.update(self.Summary)
                    
    @on(Select.Changed, "#SSID-Select")
    def on_ssid_selected(self, event: Select.Changed) -> None:
        self.selected_ssid = event.value

    @on(Input.Changed, "#EnterWLANPassword")
    def handle_selection(self, event: Input.Changed) -> None:
        self.entered_password = event.value
        
    @on(Button.Pressed, "#ConnectWLANButton") # AI telld me about @on
    def on_password_changed(self, event: Button.Pressed,):
        if event.button.id == "ConnectWLANButton":
            ConnectionStatus = self.query_one("#ConnectionStatus", Static)
            ConnectionStatus.styles.display = "none"
            interface = self.selected_interface
            password = self.entered_password
            ssid = self.selected_ssid
            password_quoted = '"' + password + '"' #Ai told me how to add Quotes to a Variable
            ssid_quoted = '"' + ssid + '"'
            try:              #Ai told about try and exept
                subprocess.run(
                ["iwctl", "--passphrase", password_quoted, "station", interface, "connect", ssid],
                check=True
                )
                ConnectionStatus.update("Connection Established")
                ConnectionStatus.styles.color = "#8DA101"
                InternetConnected = True
            except subprocess.CalledProcessError:
                ConnectionStatus.update("Connection Failed")
                ConnectionStatus.styles.color = "#F85552"
            ConnectionStatus.styles.display = "block"

    @on(SelectionList.SelectedChanged)
    def update_selected_sofware(self, event: SelectionList.SelectedChanged) -> None:
        self.selected_Software_Array = self.query_one("#select_software", SelectionList).selected

    @on(Button.Pressed, "#StartPostInstallScreen")
    def on_button_pressed(self, event: Button.Pressed) -> None:
        missing = [name for name, done in self.Needed_To_Start.items() if not done] #AI
        if missing:
            self.app.push_screen(NeededInfosScreen(missing))    #AI
        else:
            self.app.push_screen(PostInstallScreen())   #AI

class NeededInfosScreen(Screen):
    def __init__(self, missing: list[str]) -> None:
        super().__init__()
        self.missing = missing

    def compose(self):
        yield Logo()
        with Container(id="button2area"):
            lines = "\n".join( #AI
                f"[#F85552]{name.replace('_', ' ')}[/#F85552]" for name in self.missing #AI
            )
            yield Static("Still missing:\n" + lines, id="NeededInfos")
            yield Button("Go Back", id="GoBack")

    @on(Button.Pressed, "#GoBack")
    def on_GoBack_Button_Pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()   #AI 

# Asks if you really want to install Apple Puff
class PostInstallScreen(Screen):
    def compose(self):
        yield Logo()
        with Container(id="button2area"):
            yield Static("Are You Sure you want to Install Apple Puff Linux?")
            yield Static("[#F85552]Everything on the Selected Disk will be Ereased[/#F85552]")
            yield Button("Go Back", id="GoBack")
            yield Button("Start Install", id="StartInstallScreen")

    @on(Button.Pressed, "#StartInstallScreen")
    def on_start_install(self, event: Button.Pressed) -> None:
        self.app.push_screen(InstallScreen())

    @on(Button.Pressed, "#GoBack")
    def on_go_back(self, event: Button.Pressed) -> None:
        self.app.pop_screen()

def InstallResult(ResultStr):
    InstallErrors = InstallScreen().query_one("#InstallErrors", Static)
    if "Complete" in ResultStr:
        InstallErrors.update( + "\n [#F85552]", ResultStr, "[/#F85552]")
        return(True)
    else:
        InstallErrors.update(+ "\n [#93B259]", ResultStr, "[/#93B259]")
        return(False)

def InstallResult_no_InstallEorror(ResultStr):
    InstallErrors = InstallScreen().query_one("#InstallErrors", Static)
    if "Complete" in ResultStr:
        return(True)
    else:
        return(False)

def Partition_the_Drive(Disk, Partitiontable):
    DiskCommandGPT = "parted -s /dev/" + Disk + " mklabel gpt" + "mkpart primary FAT32 1MiB 1GiB mkpart primary swap 1GiB 3GiB mkpart primary ext4 3GiB 100% && mkfs.fat -F 32 /dev/" + Disk + "1 && mkswap /dev/" + Disk + "2 && mkfs.ext4 /dev/" + Disk + "3"
    DiskCommandMBR = "parted -s /dev/" + Disk + " mklabel msdos" + "mkpart primary swap 1MiB 2GiB mkpart primary ext4 2GiB 100% && mkswap /dev/" + Disk + "1 && mkfs.ext4 /dev/" + Disk + "2"
    if Partitiontable == "MBR":
        subprocess.run(DiskCommandMBR, shell=True, check=True)
        return("Partitioning Complete")
    elif Partitiontable == "GPT":
        subprocess.run(DiskCommandGPT, shell=True, check=True)
        return("Partitioning Complete")
    else:
        return("Partitioning Failed")

def Mount_the_Partitions(Disk, Partitiontable):
    MountCommandMBR = "mount /dev/" + Disk + "2 /mnt && swapon /dev/" + Disk + "1"
    MountCommandGPT = "mount /dev/" + Disk + "3 /mnt && mount --mkdir /dev/" + Disk + "2 /mnt/boot && swapon /dev/" + Disk + "1"
    if Partitiontable == "MBR":
        subprocess.run(MountCommandMBR, shell=True)
        return("Mounting Complete")
    elif Partitiontable == "GPT":
        subprocess.run(MountCommandGPT, shell=True)
        return("Mounting Complete")
    else:
        return("Mounting Failed")

def InstallSoftware(SoftwareArray):
    SoftwareCommand = "pacstrap -K /mnt base linux linux-firmware iwd sudo man base-devel git libx11 libxft xorg-server xorg-xinit pipewire pipewire-pulse pipewire-alsa pipewire-jack wireplumber rtkit grub"
    for Software in SoftwareArray:
        SoftwareCommand = SoftwareCommand + " " + Software
        try:
            subprocess.run(SoftwareCommand)
            return("Installation Complete")
        except subprocess.CalledProcessError as Error:
            Error = str(Error)
            return("Installation Failed: ", Error)

def GenerateFstab():
    try:
        subprocess.run("genfstab -U /mnt >> /mnt/etc/fstab")
        return("Generate Fstab Complete")
    except subprocess.CalledProcessError as Error:
        Error = str(Error)
        return("Generate Fstab Failed: ", Error)

def run_in_chroot(mount_path, command):
    full_command = "arch-chroot -S " + mount_path + command
    try:
        subprocess.run(full_command)
        return("Complete")
    except subprocess.CalledProcessError as Error:
        Error = str(Error)
        return("Failed" + Error)
    
# dwm installation
# systemctl --user enable --now pipewire.service pipewire-pulse.service wireplumber.service

def ContinueInstall(FuntionToUse):
    Result = FuntionToUse
    Continue = InstallResult(Result)
    if Continue == False:
        return()

def ContinueInstall_no_InstallEorror(FuntionToUse):
    Result = FuntionToUse
    Continue = InstallResult_no_InstallEorror(Result)
    if Continue == False:
        return()

def Set_Locale(TimeZone, Locale, Keymap, Hostname):
    Command_TimeZone = ""
    Command_Locale = ""
    Command_Keymap = ""
    Command_Hostname = ""
    if ContinueInstall_no_InstallEorror(run_in_chroot("/mnt", Command_TimeZone)) == False:
        return("Failed to Set TimeZone")
    if ContinueInstall_no_InstallEorror(run_in_chroot("/mnt", Command_Keymap)) == False:
        return("Failed to Set Keymap")    
    if ContinueInstall_no_InstallEorror(run_in_chroot("/mnt", Command_Locale)) == False:
        return("Failed to Set Locale")    
    if ContinueInstall_no_InstallEorror(run_in_chroot("/mnt", Command_Hostname)) == False:
        return("Failed to Set Hostname")
    return("Set Locale Complete")

def Set_Root_PW(Password):
    try:
        subprocess.run("echo " + '"' + "root:" + Password + '"' + " | " + "Arch-chroot -S /mnt chpasswd", shell=True)
    except subprocess.CalledProcessError as Error:
        Error = str(Error)
        return("Installation Failed: ", Error)


def Create_User():
    print()

def Install_Grub():
    print()

#Installs ApplePuff
class InstallScreen(Screen):
    def compose(self):
        yield Logo()
        with Container():
            yield Static("WIP")
            yield Static(id="InstallStep")
            yield Static(id="InstallErrors")
            yield Button("Back", id="WIPBack")
            yield Button("Start Install", id="StartInstall")
            yield LoadingIndicator()
            
    @on(Button.Pressed, "#StartInstall")
    def on_button_pressed(self, event: Button.Pressed,):
        InstallErrors = self.query_one("#InstallErrors", Static)
        InstallErrors.styles.display = "block"
        InstallErrors.styles.color = "#5c6a72"
        InstallStep = self.query_one("#InstallStep", Static)
        
        if event.button.id == "WIPBack":
            self.app.push_screen(PostInstallScreen())
        if event.button.id == "StartInstall":
            InstallStep.update("Partitioning the Drive...")
            if ContinueInstall(Partition_the_Drive(SeconndScreen().Selected_disk, SeconndScreen().selected_PartitionTable)) == False:
                return()
            InstallStep.update("Mounting the Drive...")
            if ContinueInstall(Mount_the_Partitions(SeconndScreen().Selected_disk, SeconndScreen().selected_PartitionTable)) == False:
                return()
            InstallStep.update("Install Software...")
            if ContinueInstall(InstallSoftware(SeconndScreen().selected_Software_Array)) == False:
                return
            InstallStep.update("Generate Fstab...")
            if ContinueInstall(GenerateFstab()) == False:
                return
            InstallStep.update("Set Locale...")
            if ContinueInstall(Set_Locale(SeconndScreen().selected_TimeZone, "en_US.UTF-8", SeconndScreen().selected_layout, SeconndScreen().selected_Hostname)) == False:
                return
            InstallStep.update("Set Root Password...")
            if ContinueInstall(Set_Root_PW(SeconndScreen().selected_RootPassword)) == False:
                return
            

def on_mount(self) -> None:                                             #AI
    self.query_one(TabbedContent).query_one(Tabs).can_focus = False     #AI

def action_prev_tab(self) -> None:                                      #AI
    self.query_one(TabbedContent).query_one(Tabs).action_previous_tab() #AI (Noted how it Works in the Obsidian Vault)

def action_next_tab(self) -> None:                                      #AI
    self.query_one(TabbedContent).query_one(Tabs).action_next_tab()     #AI (Noted how it Works in the Obsidian Vault)

class ArchInstaller(App):
        CSS_PATH = "Stylesheet.tcss"
        BINDINGS = [                                            #AI helped me with Bindings (Noted how it Works in the Obsidian Vault)
        Binding("left", "focus_previous", "Focus previous"),    # 
        Binding("right", "focus_next", "Focus next"),           #
        Binding("up", "focus_previous", "Focus previous"),
        Binding("down", "focus_next", "Focus next"),
        ]
        def on_mount(self) -> None:
            self.push_screen(StartScreen())

        # Arrowkeys for Navigation (Original Keys)
        #def _on_key(self, event):
        #    match event.key:
        #        case "down":
        #            self.action_focus_next()
        #        case "up":
        #            self.action_focus_previous()
    
if __name__ == "__main__":
    app = ArchInstaller()
    app.run()
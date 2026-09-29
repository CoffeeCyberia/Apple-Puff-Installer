# Ill try to use as little AI as Possible but Sometimes my skills arent good enought.
# But everything ill Code with AI will get Noted in Obsidian. You Can find my Notes for this Project in the Reposetory
# Thx for using this Programm. If you have some Correction for my code feel free to Edit and commit you Changes.

import os
from textual.binding import Binding
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static, Button, Label, TabbedContent, TabPane, RadioButton, RadioSet, Tabs, Select, Input, SelectionList
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

class SeconndScreen(Screen):
    # Variables for Summary Screen
    selected_TimeZone: str | None = None
    selected_layout: str | None = None
    InternetConnected = False
    Selected_disk: str | None = None
    # Variables for Functions
    selected_ssid: str | None = None
    selected_interface: str | None = None
    entered_password: str | None = None
    selected_PartitionTable: str | None = None
    Summary = "Timezone: ",selected_TimeZone , "\n", "Selected Keyboard Layout: ", selected_layout, "\n", "Slected Disk to install Apple Puff on: ", Selected_disk, "\n", "Internet Connected: ",InternetConnected, "\n"
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
                        yield Select(options=["GPT","MBR"], id="PartitionTable", classes="select1")
            with TabPane("User Creation", classes="InstallationTabs"):
                with Container(id="button2area"):
                    yield Input(placeholder="Enter Username", id="EnterUsername", classes="select1")
                    yield Input(placeholder="Enter Password", id="EnterUserPassword", password=True, classes="select1")
                    yield Input(placeholder="Enter Password Again", id="EnterUserPassword2", password=True, classes="select1")
                    yield Input(placeholder="Enter Root Password", id="EnterRootPassword", password=True, classes="select1")
                    yield Input(placeholder="Enter Toor Password Again", id="EnterRootPassword2", password=True, classes="select1")
                    yield Input(placeholder="Enter Hostname", id="EnterHostname", classes="select1")
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
                        ("Firefox", 0, True),
                        ("Obsidian", 1),
                        ("NeoVim", 2, True),
                        ("LibreOffice", 3),
                        ("Btop", 4, True),
                        ("cmus", 5, True)

                    )
            with TabPane("Summary", classes="InstallationTabs"):
                with Container(id="button2area"):
                    yield Static(classes="SummaryLabel", id="SummaryLabel")
                    yield Button("Start Install", classes="button1", id="StartInstallScreen")

    @on(Input.Changed, "#TimeZoneInput")                            #AI
    def on_TimeZone_changed(self, event: Input.Changed) -> None:      #
        self.selected_TimeZone = event.value
        SummaryScreen = self.query_one("#SummaryLabel", Static)
        SummaryScreen.update(self.Summary)
        subprocess.run("timedateclt set-timezone " + event.value)

    @on(Input.Changed, "#KeyboardLayoutInput")                      #AI
    def on_layout_changed(self, event: Input.Changed) -> None:      #
        self.selected_layout = event.value                          #
        SummaryScreen = self.query_one("#SummaryLabel", Static)
        SummaryScreen.update(self.Summary)     
        subprocess.run("loadkeys " + event.value)


    @on(RadioButton.Changed, "#SelectDisk")
    def on_disk_changed(self, event: RadioButton.Changed) -> None:
        self.Selected_disk = event.value
        SummaryScreen = self.query_one("#SummaryLabel", Static)
        SummaryScreen.update(self.Summary) 

    @on(Select.Changed, "#PartitionTable")
    def on_Partition_Table_changed(self, event: Select.Changed) -> None:
        self.selected_PartitionTable = event.value

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
            self.selected_interface = event.value
             
            subprocess.run(
            ["sudo", "iwctl", "station", event.value, "scan"]
            )
            output = subprocess.check_output(
                ["sh", "-c", r"""iwctl station "$1" get-networks | sed 's/\x1b\[[0-9;]*m//g' | tail -n +5 | sed 's/^[ >]*//; s/ \{2,\}.*//' | grep -v '^$'""", "sh", event.value],  #AI
                text=True,
            )
            new_options = [line for line in output.splitlines() if line.strip()] #AI

            SSID_select.set_options((s, s) for s in new_options)  #AI
            SSID_select.clear                                     #AI
            SSID_select.styles.display = "block"                  #AI
            Password_Input.clear   
            Password_Input.styles.display = "block"
            Connect_Button.styles.display = "block"
            
        elif "en" in event.value:
            ConnectionStatus.styles.display = "none"
            command = "/sys/class/net/" + event.value + "/operstate"
            LANOUT = subprocess.check_output(
            ["cat", command],
            text=True,
            ).strip()
            
            if LANOUT == "up":
                ConnectionStatus.update("Internet Connected")
                ConnectionStatus.styles.color = "#8DA101"
                InternetConnected = True
                
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
                ["sudo", "iwctl", "--passphrase", password_quoted, "station", interface, "connect", ssid],
                check=True
                )
                ConnectionStatus.update("Connection Established")
                ConnectionStatus.styles.color = "#8DA101"
                InternetConnected = True
            except subprocess.CalledProcessError:
                ConnectionStatus.update("Connection Failed")
                ConnectionStatus.styles.color = "#F85552"
            ConnectionStatus.styles.display = "block"

    @on(Button.Pressed, "#StartInstallScreen")
    def on_button_pressed(self, event: Button.Pressed,):
        if event.button.id == "StartInstallScreen":
            self.app.push_screen(PostInstallScreen())

class PostInstallScreen(Screen):
    def compose(self):
        yield Logo()
        with Container(id="button2area"):
            yield Static("Are You Sure you want to Install Apple Puff Linux?")
            yield Static("[#F85552]Everything on the Selected Disk will be Ereased[/#F85552]")
            yield Button("Go Back", id="GoBack")
            yield Button("Start Install", id="StartInstall")
    @on(Button.Pressed, "#StartInstallScreen")
    def on_button_pressed(self, event: Button.Pressed,):
        if event.button.id == "StartInstall":
            self.app.push_screen(InstallScreen())
        if event.button.id == "GoBack":
            self.app.push_screen(SeconndScreen())

def Partition_the_Drive(Disk, Partitiontable,):
    DiskCommandGPT = "parted -s /dev/" + SeconndScreen().Selected_disk + " mklabel gpt" + "mkpart primary FAT32 1MiB 1GiB mkpart primary swap 1GiB 3GiB mkpart primary ext4 3GiB 100% && mkfs.fat -F 32 /dev/" + SeconndScreen().Selected_disk + "1 && sudo mkswap /dev/" + SeconndScreen().Selected_disk + "2 && sudo mkfs.ext4 /dev/" + SeconndScreen().Selected_disk + "3"
    DiskCommandMBR = "parted -s /dev/" + SeconndScreen().Selected_disk + " mklabel mbr" + "mkpart primary swap 1MiB 2GiB mkpart primary ext4 2GiB 100% && sudo mkswap /dev/" + SeconndScreen().Selected_disk + "1 && sudo mkfs.ext4 /dev/" + SeconndScreen().Selected_disk + "2"
    if SeconndScreen().selected_PartitionTable == "MBR":
        subprocess.run(DiskCommandMBR, shell=True)
        return("Complete")
    elif SeconndScreen().selected_PartitionTable == "GPT":
        subprocess.run(DiskCommandGPT, shell=True)
        return("Complete")
    else:
        return("Failed")


class InstallScreen(Screen):

    def compose(self):
        yield Logo
        with Container:
            yield Static("WIP")
            yield Static(id="InstallErrors")
            yield Button("Back", id="WIPBack")
            


    @on(Button.Pressed, "#StartInstallScreen")
    def on_button_pressed(self, event: Button.Pressed,):
        InstallErrors = self.query_one("#InstallErrors", Static)
        InstallErrors.styles.display = "block"
        InstallErrors.styles.color = "#5c6a72"
        InstallErrors.update("Partitioning the Drive...")
        if event.button.id == "WIPBACK":
            self.app.push_screen(PostInstallScreen())
        if event.button.id == "StartInstall":
            if SeconndScreen().selected_PartitionTable == "MBR":
                subprocess.run(self.DiskCommandMBR, shell=True)
            elif SeconndScreen().selected_PartitionTable == "GPT":
                subprocess.run(self.DiskCommandGPT, shell=True)
            else:
                InstallErrors.update("Did you Select if your Disk should be MBR or GPT?")
                InstallErrors.styles.color = "#F85552"

        
        
                
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
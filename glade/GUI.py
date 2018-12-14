import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:

    global builder
    
    # New Session Code
    
    def new_session_overlay(self, button):
        dialog = builder.get_object('new_session_overlay')
        response = dialog.run()
        print(response)
        dialog.hide()
        
                
    def close_new_session(self, button):
        dialog = builder.get_object('new_session_overlay')
        dialog.hide()
        
    def create_new_session(self, button):
        new_session_name = builder.get_object('new_session_name')
        new_session_desc = builder.get_object('new_session_description')
        session_name = new_session_name.get_text()
        session_description = new_session_desc.get_text()
        print(session_name)
        print(session_description)
        dialog = builder.get_object('new_session_overlay')
        dialog.hide()
        
    # End of New Session Code
    
    # Existing Session Code
    
    def open_session_overlay(self, button):
        dialog = builder.get_object('open_session_overlay')
        response = dialog.run()
        print(response)
        dialog.hide()

    def close_session(self, button):
        dialog = builder.get_object('open_session_overlay')
        dialog.hide()
        
    def open_existing_session(self, button):
        session_path = builder.get_object('existing_session_path')
        filepath = session_path.get_text()
        print(filepath)
        dialog = builder.get_object('open_session_overlay')
        dialog.hide()
        
    # End of Existing Session Code
    
    # Switch Workplace Code

    def workspace_launcher_overlay(self, button):
        dialog = builder.get_object('workspace_launcher_overlay')
        response = dialog.run()
        print(response)
        dialog.hide()
        
    def launch_workspace(self, button):
        dialog = builder.get_object('workspace_launcher_overlay')
        workspace_dir = builder.get_object('workspace_dir')
        workspace_dest_name = builder.get_object('workspace_dest_name')
        workspace_dir_path = builder.get_object('workspace_dir_path')
        workspace_dir = workspace_dir.get_text()
        workspace_dest_name = workspace_dest_name.get_text()
        workspace_dir_path = workspace_dir_path.get_text()
        print(workspace_dir)
        print(workspace_dest_name)
        print(workspace_dir_path)
        dialog.hide()
        
    def close_workspace_launcher(self, button):
        dialog = builder.get_object('workspace_launcher_overlay')
        dialog.hide() 
        
    # End of Switch Workplace Code
    
    # PCAP Overlay Code
    
    def pcap_overlay(self, button):
        dialog = builder.get_object('pcap_overlay')
        response = dialog.run()
        print(response)
        dialog.hide()
        
    def pcap_close(self, button):
        dialog = builder.get_object('pcap_overlay')
        dialog.hide() 
    
    def convert_pdml(self, button):
        dialog = builder.get_object('pcap_overlay')
        pcap_file = builder.get_object('pcap_file')
        dissector = builder.get_object('dissector')
        pcap_file = pcap_file.get_text()
        dissector = dissector.get_text()
        print(pcap_file)
        print(dissector)
        dialog.hide()
        
    # End of PCAP Overlay Code

    def terminal_overlay(self, button):
        if os.name == 'nt':
            os.system("start cmd")
        elif os.name == 'posix':
            os.system("x-terminal-emulator -e /bin/bash")

    def stage_one_setup(self, button):
        multi_set_show(builder, True,
                            "filter_area",
                            "packet_area",
                            "field_area",
                            "new_tab")
        multi_set_show(builder, False,
                            "dependency_tab",
                            "template_tab",
                            "state_machine",
                            "equivalency_tab",
                            "generation_tab")

    def stage_two_setup(self, button):
        multi_set_show(builder, True,
                            "packet_area",
                            "field_area",
                            "dependency_tab",
                            "template_tab")
        multi_set_show(builder, False,
                            "filter_area",
                            "new_tab",
                            "state_machine",
                            "equivalency_tab",
                            "generation_tab")

    def stage_three_setup(self, button):
        multi_set_show(builder, True,
                           "state_machine",
                            "field_area",
                            "equivalency_tab")
        multi_set_show(builder, False,
                            "filter_area",
                            "field_area",
                            "new_tab",
                            "dependency_tab",
                            "template_tab",
                            "generation_tab",
                            "packet_area")
        
        state_machine = builder.get_object('state_machine')
        state_machine.set_from_file("")
    

    def stage_four_setup(self, button):
        multi_set_show(builder, True,
                            "generation_tab")
        multi_set_show(builder, False,
                            "filter_area",
                            "template_tab",
                            "packet_area",
                            "field_area",
                            "new_tab",
                            "dependency_tab",
                            "template_tab",
                            "state_machine",
                            "equivalency_tab")

    def pdml_state_save_as(self, button):
        print("pdml_state_save_as")

    def pdml_state_save(self, button):
        print("pdml_state_save")

    def pdml_state_close(self, button):
        print("pdml_state_close")

    def pdml_state_delete(self, button):
        print("pdml_state_delete")

    def pdml_state_rename(self, button):
        print("pdml_state_rename")

    def filter_apply(self, button):
        print("filter_apply")

    def filter_clear(self, button):
        print("filter_apply")

    def filter_save(self, button):
        print("filter_apply")

    def saved_filter_apply(self, button):
        print("filter_apply")

    def packet_remove(self, button):
        print("packet_remove")

    def packet_clear(self, button):
        print("packet_clear")

    def tag_area_update(self, button):
        print("tag_area_update")

    def tag_area_cancel(self, button):
        print("tag_area_cancel")

        
    def add_session_tree(self, button):
        print("add session")
        tree = builder.get_object('session_view_tree')
        tree.add_column_name("Session A",0)

builder = Gtk.Builder()
builder.add_from_file("UIFiles/NTBSG_Main.glade")


def multi_set_show(obj, show, *args):
    for arg in args:
        if show:
            obj.get_object(arg).show()
        else:
            obj.get_object(arg).hide()

#store = Gtk.ListStore(str, int)
#fakelist = [["Fake thingy", 3], ["Other fake thingy", 5]]
#
#for item in fakelist:
#    store.append(item)
#    
#for row in store:
#    #Print values of all columns
#    print(row[:])
    

            
main_window = builder.get_object("main_window")
builder.connect_signals(Handler())
## multi_set_show(builder, False, 'label1', 'label2')
main_window.show_all()
multi_set_show(builder, True,
                            "filter_area",
                            "packet_area",
                            "field_area",
                            "new_tab")
multi_set_show(builder, False,
                            "dependency_tab",
                            "template_tab",
                            "state_machine",
                            "equivalency_tab",
                            "generation_tab")
# multi_set_show(builder, False,
#                     "filter_area",
#                     "packet_area",
#                     "field_area_section",
#                     "new_tab",
#                     "dependency_tab",
#                     "template_tab",
#                     # #"state_machine_area",
#                     "equivalency_tab",
#                     "generation_tab")


Gtk.main()














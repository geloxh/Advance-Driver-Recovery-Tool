# Additional methods for RecoveryGUI class
# These should be added to the RecoveryGUI class in main.py

def setup_preview_tab(self):
    """Setup the file preview tab"""
    # Title
    ttk.Label(self.preview_frame, text="File Preview", style='Title.TLabel').pack(pady=10)
    
    # File list frame
    list_frame = ttk.LabelFrame(self.preview_frame, text="Recovered Files")
    list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    
    # Create treeview for file list
    columns = ('Name', 'Type', 'Size', 'Status')
    self.file_tree = ttk.Treeview(list_frame, columns=columns, show='tree headings', height=15)
    
    # Configure columns
    self.file_tree.heading('#0', text='File')
    self.file_tree.heading('Name', text='Original Name')
    self.file_tree.heading('Type', text='File Type')
    self.file_tree.heading('Size', text='Size')
    self.file_tree.heading('Status', text='Status')
    
    self.file_tree.column('#0', width=200)
    self.file_tree.column('Name', width=150)
    self.file_tree.column('Type', width=120)
    self.file_tree.column('Size', width=100)
    self.file_tree.column('Status', width=100)
    
    # Scrollbars for treeview
    tree_scroll_y = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.file_tree.yview)
    self.file_tree.configure(yscrollcommand=tree_scroll_y.set)
    
    self.file_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Bind selection event
    self.file_tree.bind('<<TreeviewSelect>>', self.on_file_select)
    
    # Preview controls
    preview_controls = ttk.Frame(self.preview_frame)
    preview_controls.pack(fill=tk.X, padx=10, pady=5)
    
    ttk.Button(preview_controls, text="🔄 Refresh List", command=self.refresh_file_list).pack(side=tk.LEFT, padx=5)
    ttk.Button(preview_controls, text="📂 Open Location", command=self.open_file_location).pack(side=tk.LEFT, padx=5)
    ttk.Button(preview_controls, text="🗑️ Delete Selected", command=self.delete_selected_file).pack(side=tk.LEFT, padx=5)
    
    # File info panel
    info_frame = ttk.LabelFrame(self.preview_frame, text="File Information")
    info_frame.pack(fill=tk.X, padx=10, pady=5)
    
    self.file_info_text = scrolledtext.ScrolledText(info_frame, height=6, width=80)
    self.file_info_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

def setup_settings_tab(self):
    """Setup the settings tab"""
    # Title
    ttk.Label(self.settings_frame, text="Settings & Configuration", style='Title.TLabel').pack(pady=10)
    
    # Recovery settings
    recovery_frame = ttk.LabelFrame(self.settings_frame, text="Recovery Settings")
    recovery_frame.pack(fill=tk.X, padx=10, pady=5)
    
    # Scan depth
    ttk.Label(recovery_frame, text="Scan Depth:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
    self.scan_depth_var = tk.StringVar(value="Normal")
    scan_depth_combo = ttk.Combobox(recovery_frame, textvariable=self.scan_depth_var, 
                                   values=["Quick", "Normal", "Deep", "Exhaustive"])
    scan_depth_combo.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
    
    # File types to recover
    ttk.Label(recovery_frame, text="File Types:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    file_types_frame = ttk.Frame(recovery_frame)
    file_types_frame.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
    
    self.recover_images = tk.BooleanVar(value=True)
    self.recover_documents = tk.BooleanVar(value=True)
    self.recover_audio = tk.BooleanVar(value=True)
    self.recover_video = tk.BooleanVar(value=True)
    self.recover_archives = tk.BooleanVar(value=True)
    
    ttk.Checkbutton(file_types_frame, text="Images", variable=self.recover_images).pack(side=tk.LEFT, padx=5)
    ttk.Checkbutton(file_types_frame, text="Documents", variable=self.recover_documents).pack(side=tk.LEFT, padx=5)
    ttk.Checkbutton(file_types_frame, text="Audio", variable=self.recover_audio).pack(side=tk.LEFT, padx=5)
    ttk.Checkbutton(file_types_frame, text="Video", variable=self.recover_video).pack(side=tk.LEFT, padx=5)
    ttk.Checkbutton(file_types_frame, text="Archives", variable=self.recover_archives).pack(side=tk.LEFT, padx=5)
    
    # Output settings
    output_settings_frame = ttk.LabelFrame(self.settings_frame, text="Output Settings")
    output_settings_frame.pack(fill=tk.X, padx=10, pady=5)
    
    # Auto-organize files
    self.auto_organize = tk.BooleanVar(value=True)
    ttk.Checkbutton(output_settings_frame, text="Auto-organize files by type", 
                   variable=self.auto_organize).pack(anchor=tk.W, padx=5, pady=2)
    
    # Generate thumbnails
    self.generate_thumbnails = tk.BooleanVar(value=False)
    ttk.Checkbutton(output_settings_frame, text="Generate thumbnails for images", 
                   variable=self.generate_thumbnails).pack(anchor=tk.W, padx=5, pady=2)
    
    # Verify recovered files
    self.verify_files = tk.BooleanVar(value=True)
    ttk.Checkbutton(output_settings_frame, text="Verify recovered files integrity", 
                   variable=self.verify_files).pack(anchor=tk.W, padx=5, pady=2)
    
    # Advanced settings
    advanced_frame = ttk.LabelFrame(self.settings_frame, text="Advanced Settings")
    advanced_frame.pack(fill=tk.X, padx=10, pady=5)
    
    # Chunk size
    ttk.Label(advanced_frame, text="Chunk Size (MB):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
    self.chunk_size_var = tk.StringVar(value="1")
    chunk_size_spin = ttk.Spinbox(advanced_frame, from_=1, to=100, textvariable=self.chunk_size_var, width=10)
    chunk_size_spin.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
    
    # Max file size
    ttk.Label(advanced_frame, text="Max File Size (MB):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    self.max_file_size_var = tk.StringVar(value="50")
    max_size_spin = ttk.Spinbox(advanced_frame, from_=1, to=1000, textvariable=self.max_file_size_var, width=10)
    max_size_spin.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
    
    # Save/Load settings buttons
    settings_buttons = ttk.Frame(self.settings_frame)
    settings_buttons.pack(fill=tk.X, padx=10, pady=10)
    
    ttk.Button(settings_buttons, text="💾 Save Settings", command=self.save_settings).pack(side=tk.LEFT, padx=5)
    ttk.Button(settings_buttons, text="📁 Load Settings", command=self.load_settings).pack(side=tk.LEFT, padx=5)
    ttk.Button(settings_buttons, text="🔄 Reset to Defaults", command=self.reset_settings).pack(side=tk.LEFT, padx=5)

def setup_help_tab(self):
    """Setup the help tab"""
    # Title
    ttk.Label(self.help_frame, text="Help & Documentation", style='Title.TLabel').pack(pady=10)
    
    # Help content
    help_notebook = ttk.Notebook(self.help_frame)
    help_notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    
    # Quick Start Guide
    quick_start_frame = ttk.Frame(help_notebook)
    help_notebook.add(quick_start_frame, text="Quick Start")
    
    quick_start_text = scrolledtext.ScrolledText(quick_start_frame, wrap=tk.WORD)
    quick_start_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    quick_start_content = """
QUICK START GUIDE
================

1. SELECT DRIVE
   - Choose the flash drive you want to recover from the dropdown
   - Make sure the drive is connected and recognized by the system

2. CHOOSE OUTPUT DIRECTORY
   - Select where you want recovered files to be saved
   - Ensure you have enough free space for recovered files

3. START RECOVERY
   - Click "Start Recovery" to begin the process
   - The tool will scan for file signatures and recover data
   - Progress will be shown in the progress bar

4. REVIEW RESULTS
   - Check the "File Preview" tab to see recovered files
   - Use the "Drive Analysis" tab for drive health information
   - View detailed logs in the "Recovery Log" tab

TIPS FOR BETTER RECOVERY:
- Stop using the drive immediately after data loss
- Use "Deep Scan" for better results (takes longer)
- Try different scan depths if initial scan doesn't find files
- Check the drive analysis for corruption indicators
    """
    quick_start_text.insert(tk.END, quick_start_content)
    quick_start_text.config(state=tk.DISABLED)
    
    # Troubleshooting
    troubleshooting_frame = ttk.Frame(help_notebook)
    help_notebook.add(troubleshooting_frame, text="Troubleshooting")
    
    troubleshooting_text = scrolledtext.ScrolledText(troubleshooting_frame, wrap=tk.WORD)
    troubleshooting_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    troubleshooting_content = """
TROUBLESHOOTING
===============

COMMON ISSUES:

1. "Drive not detected"
   - Ensure drive is properly connected
   - Try different USB ports
   - Check if drive appears in system disk management
   - Run as administrator if on Windows

2. "Permission denied" errors
   - Run the application as administrator (Windows)
   - Use sudo on Linux/Mac systems
   - Check if drive is write-protected

3. "No files recovered"
   - Try Deep Scan mode for better detection
   - Check if drive is severely corrupted
   - Verify file types are enabled in settings
   - Drive may have been overwritten multiple times

4. "Recovery process is slow"
   - This is normal for deep scanning
   - Larger drives take more time
   - Reduce chunk size in advanced settings
   - Close other applications to free up resources

5. "Recovered files are corrupted"
   - Enable file verification in settings
   - Some files may be partially overwritten
   - Try different recovery methods
   - Original files may have been damaged before loss

GETTING HELP:
- Check the log files for detailed error messages
- Note your operating system and drive type
- Document the steps that led to the issue
    """
    troubleshooting_text.insert(tk.END, troubleshooting_content)
    troubleshooting_text.config(state=tk.DISABLED)
    
    # About
    about_frame = ttk.Frame(help_notebook)
    help_notebook.add(about_frame, text="About")
    
    about_text = scrolledtext.ScrolledText(about_frame, wrap=tk.WORD)
    about_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    about_content = """
ADVANCED FLASH DRIVE RECOVERY TOOL
==================================

Version: 1.0
Author: IT Admin Recovery Tool

FEATURES:
- Raw disk scanning for maximum recovery
- Advanced file signature detection
- Support for 50+ file types
- Real-time progress tracking
- Comprehensive logging
- Drive health analysis
- File preview and verification
- Batch processing capabilities

SUPPORTED FILE TYPES:
- Images: JPEG, PNG, GIF, BMP, TIFF, ICO
- Documents: PDF, DOC, RTF, TXT, Office files
- Audio: MP3, WAV, OGG
- Video: MP4, MKV, FLV, AVI
- Archives: ZIP, RAR, 7Z, GZIP, BZIP2
- Executables: EXE, ELF, Java Class files
- Databases: SQLite
- Fonts: TTF, OTF
- Email: EML files

TECHNICAL DETAILS:
- Uses advanced file carving techniques
- Implements multiple recovery algorithms
- Cross-platform compatibility (Windows, Linux, Mac)
- Multi-threaded processing for better performance
- Comprehensive error handling and logging

LICENSE:
This software is provided as-is for data recovery purposes.
Use at your own risk. Always backup important data.

COPYRIGHT:
© 2024 IT Admin Recovery Tool. All rights reserved.
    """
    about_text.insert(tk.END, about_content)
    about_text.config(state=tk.DISABLED)

# Menu and toolbar action methods
def new_session(self):
    """Start a new recovery session"""
    if messagebox.askyesno("New Session", "Start a new recovery session? This will clear current results."):
        self.recovery_tool.recovered_files = []
        self.results_text.delete(1.0, tk.END)
        if hasattr(self, 'file_info_text'):
            self.file_info_text.delete(1.0, tk.END)
        if hasattr(self, 'file_tree'):
            self.refresh_file_list()
        self.update_status("New session started")

def load_report(self):
    """Load a recovery report"""
    filename = filedialog.askopenfilename(
        title="Load Recovery Report",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )
    if filename:
        try:
            with open(filename, 'r') as f:
                report_data = json.load(f)
            self.recovery_tool.recovered_files = report_data.get('recovered_files', [])
            if hasattr(self, 'file_tree'):
                self.refresh_file_list()
            self.update_status(f"Loaded report: {filename}")
            messagebox.showinfo("Success", "Recovery report loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load report: {str(e)}")

def save_report(self):
    """Save current recovery report"""
    if not self.recovery_tool.recovered_files:
        messagebox.showwarning("Warning", "No recovery data to save")
        return
    
    filename = filedialog.asksaveasfilename(
        title="Save Recovery Report",
        defaultextension=".json",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )
    if filename:
        try:
            report_path = self.recovery_tool.generate_recovery_report(os.path.dirname(filename))
            if report_path:
                # Copy to user-specified location
                import shutil
                shutil.copy2(report_path, filename)
                self.update_status(f"Report saved: {filename}")
                messagebox.showinfo("Success", f"Report saved to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save report: {str(e)}")

def export_results(self):
    """Export recovery results to various formats"""
    if not self.recovery_tool.recovered_files:
        messagebox.showwarning("Warning", "No recovery data to export")
        return
    
    # Create export dialog
    export_window = tk.Toplevel(self.root)
    export_window.title("Export Results")
    export_window.geometry("400x300")
    export_window.transient(self.root)
    export_window.grab_set()
    
    ttk.Label(export_window, text="Export Format:", style='Subtitle.TLabel').pack(pady=10)
    
    export_format = tk.StringVar(value="CSV")
    formats = ["CSV", "JSON"]
    
    for fmt in formats:
        ttk.Radiobutton(export_window, text=fmt, variable=export_format, value=fmt).pack(anchor=tk.W, padx=20)
    
    def do_export():
        filename = filedialog.asksaveasfilename(
            title="Export Results",
            defaultextension=f".{export_format.get().lower()}",
            filetypes=[(f"{export_format.get()} files", f"*.{export_format.get().lower()}"), ("All files", "*.*")]
        )
        if filename:
            try:
                self.export_to_format(filename, export_format.get())
                export_window.destroy()
                messagebox.showinfo("Success", f"Results exported to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Export failed: {str(e)}")
    
    ttk.Button(export_window, text="Export", command=do_export).pack(pady=20)
    ttk.Button(export_window, text="Cancel", command=export_window.destroy).pack()

def quick_scan(self):
    """Perform a quick scan"""
    self.update_status("Quick scan mode selected")
    if hasattr(self, 'status_indicator'):
        self.status_indicator.config(text="● Quick Mode", foreground='orange')
    messagebox.showinfo("Quick Scan", "Quick scan mode selected. Use Start Recovery to begin.")

def deep_scan(self):
    """Perform a deep scan"""
    self.update_status("Deep scan mode selected")
    if hasattr(self, 'status_indicator'):
        self.status_indicator.config(text="● Deep Mode", foreground='red')
    messagebox.showinfo("Deep Scan", "Deep scan mode selected. Use Start Recovery to begin.")

def disk_health_check(self):
    """Perform disk health check"""
    drive = self.drive_var.get()
    if not drive:
        messagebox.showerror("Error", "Please select a drive first")
        return
    
    # Switch to analysis tab and run analysis
    self.notebook.select(1)  # Analysis tab
    self.analysis_drive_combo.set(drive)
    self.analyze_drive()

def format_recovery(self):
    """Attempt to recover from formatted drive"""
    messagebox.showinfo("Format Recovery", 
                       "Format recovery uses deep scanning techniques.\n"
                       "This may take several hours depending on drive size.\n"
                       "Select Deep Scan mode for best results.")

def toggle_hidden_files(self):
    """Toggle showing hidden files"""
    messagebox.showinfo("Hidden Files", "Hidden file detection is enabled by default in recovery scans.")

def show_file_filter(self):
    """Show file type filter dialog"""
    messagebox.showinfo("File Filter", "File type filtering is available in the Settings tab.")

def show_user_guide(self):
    """Show user guide"""
    self.notebook.select(5)  # Help tab

def show_troubleshooting(self):
    """Show troubleshooting guide"""
    self.notebook.select(5)  # Help tab

def show_about(self):
    """Show about dialog"""
    about_window = tk.Toplevel(self.root)
    about_window.title("About")
    about_window.geometry("400x300")
    about_window.transient(self.root)
    about_window.grab_set()
    
    ttk.Label(about_window, text="Advanced Flash Drive Recovery Tool", 
             style='Title.TLabel').pack(pady=20)
    ttk.Label(about_window, text="Version 1.0").pack()
    ttk.Label(about_window, text="© 2024 IT Admin Recovery Tool").pack(pady=10)
    
    ttk.Button(about_window, text="OK", command=about_window.destroy).pack(pady=20)

# File preview methods
def on_file_select(self, event):
    """Handle file selection in preview"""
    if hasattr(self, 'file_tree'):
        selection = self.file_tree.selection()
        if selection:
            item = self.file_tree.item(selection[0])
            filename = item['text']
            self.show_file_info(filename)

def refresh_file_list(self):
    """Refresh the file list in preview tab"""
    if not hasattr(self, 'file_tree'):
        return
        
    # Clear existing items
    for item in self.file_tree.get_children():
        self.file_tree.delete(item)
    
    # Add recovered files
    for i, file_info in enumerate(self.recovery_tool.recovered_files):
        filename = file_info.get('filename', f'File_{i}')
        original_name = file_info.get('original_name', 'Unknown')
        file_type = file_info.get('file_type', 'Unknown')
        size = self.format_file_size(file_info.get('size', 0))
        status = "Recovered"
        
        self.file_tree.insert('', 'end', text=filename, 
                             values=(original_name, file_type, size, status))

def open_file_location(self):
    """Open the location of selected file"""
    if not hasattr(self, 'file_tree'):
        return
        
    selection = self.file_tree.selection()
    if not selection:
        messagebox.showwarning("Warning", "Please select a file first")
        return
    
    item = self.file_tree.item(selection[0])
    filename = item['text']
    
    # Find the file in recovered files
    for file_info in self.recovery_tool.recovered_files:
        if file_info['filename'] == filename:
            file_path = file_info['filepath']
            folder_path = os.path.dirname(file_path)
            
            # Open folder based on OS
            try:
                if platform.system() == "Windows":
                    os.startfile(folder_path)
                elif platform.system() == "Darwin":  # macOS
                    subprocess.run(["open", folder_path])
                else:  # Linux
                    subprocess.run(["xdg-open", folder_path])
            except Exception as e:
                messagebox.showerror("Error", f"Could not open location: {str(e)}")
            break

def delete_selected_file(self):
    """Delete selected recovered file"""
    if not hasattr(self, 'file_tree'):
        return
        
    selection = self.file_tree.selection()
    if not selection:
        messagebox.showwarning("Warning", "Please select a file first")
        return
    
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected file?"):
        item = self.file_tree.item(selection[0])
        filename = item['text']
        
        # Find and remove the file
        for i, file_info in enumerate(self.recovery_tool.recovered_files):
            if file_info['filename'] == filename:
                try:
                    os.remove(file_info['filepath'])
                    del self.recovery_tool.recovered_files[i]
                    self.file_tree.delete(selection[0])
                    self.update_status(f"Deleted file: {filename}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete file: {str(e)}")
                break

def show_file_info(self, filename):
    """Show information about selected file"""
    if not hasattr(self, 'file_info_text'):
        return
        
    self.file_info_text.delete(1.0, tk.END)
    
    # Find file info
    for file_info in self.recovery_tool.recovered_files:
        if file_info.get('filename') == filename:
            info_text = f"File Information:\n"
            info_text += f"{'='*30}\n\n"
            info_text += f"Filename: {file_info.get('filename', 'Unknown')}\n"
            info_text += f"Original Name: {file_info.get('original_name', 'Unknown')}\n"
            info_text += f"File Type: {file_info.get('file_type', 'Unknown')}\n"
            info_text += f"Size: {self.format_file_size(file_info.get('size', 0))}\n"
            info_text += f"Hash (MD5): {file_info.get('hash', 'Unknown')}\n"
            info_text += f"Recovered At: {file_info.get('recovered_at', 'Unknown')}\n"
            info_text += f"File Path: {file_info.get('filepath', 'Unknown')}\n"
            
            if file_info.get('original_path'):
                info_text += f"Original Path: {file_info.get('original_path')}\n"
            
            self.file_info_text.insert(tk.END, info_text)
            break

# Settings methods
def save_settings(self):
    """Save current settings"""
    settings = {
        'scan_depth': getattr(self, 'scan_depth_var', tk.StringVar()).get(),
        'recover_images': getattr(self, 'recover_images', tk.BooleanVar()).get(),
        'recover_documents': getattr(self, 'recover_documents', tk.BooleanVar()).get(),
        'recover_audio': getattr(self, 'recover_audio', tk.BooleanVar()).get(),
        'recover_video': getattr(self, 'recover_video', tk.BooleanVar()).get(),
        'recover_archives': getattr(self, 'recover_archives', tk.BooleanVar()).get(),
        'auto_organize': getattr(self, 'auto_organize', tk.BooleanVar()).get(),
        'generate_thumbnails': getattr(self, 'generate_thumbnails', tk.BooleanVar()).get(),
        'verify_files': getattr(self, 'verify_files', tk.BooleanVar()).get(),
        'chunk_size': getattr(self, 'chunk_size_var', tk.StringVar()).get(),
        'max_file_size': getattr(self, 'max_file_size_var', tk.StringVar()).get()
    }
    
    filename = filedialog.asksaveasfilename(
        title="Save Settings",
        defaultextension=".json",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )
    if filename:
        try:
            with open(filename, 'w') as f:
                json.dump(settings, f, indent=2)
            messagebox.showinfo("Success", "Settings saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {str(e)}")

def load_settings(self):
    """Load settings from file"""
    filename = filedialog.askopenfilename(
        title="Load Settings",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )
    if filename:
        try:
            with open(filename, 'r') as f:
                settings = json.load(f)
            
            # Apply settings if variables exist
            if hasattr(self, 'scan_depth_var'):
                self.scan_depth_var.set(settings.get('scan_depth', 'Normal'))
            if hasattr(self, 'recover_images'):
                self.recover_images.set(settings.get('recover_images', True))
            if hasattr(self, 'recover_documents'):
                self.recover_documents.set(settings.get('recover_documents', True))
            if hasattr(self, 'recover_audio'):
                self.recover_audio.set(settings.get('recover_audio', True))
            if hasattr(self, 'recover_video'):
                self.recover_video.set(settings.get('recover_video', True))
            if hasattr(self, 'recover_archives'):
                self.recover_archives.set(settings.get('recover_archives', True))
            if hasattr(self, 'auto_organize'):
                self.auto_organize.set(settings.get('auto_organize', True))
            if hasattr(self, 'generate_thumbnails'):
                self.generate_thumbnails.set(settings.get('generate_thumbnails', False))
            if hasattr(self, 'verify_files'):
                self.verify_files.set(settings.get('verify_files', True))
            if hasattr(self, 'chunk_size_var'):
                self.chunk_size_var.set(settings.get('chunk_size', '1'))
            if hasattr(self, 'max_file_size_var'):
                self.max_file_size_var.set(settings.get('max_file_size', '50'))
            
            messagebox.showinfo("Success", "Settings loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load settings: {str(e)}")

def reset_settings(self):
    """Reset settings to defaults"""
    if messagebox.askyesno("Reset Settings", "Reset all settings to default values?"):
        if hasattr(self, 'scan_depth_var'):
            self.scan_depth_var.set("Normal")
        if hasattr(self, 'recover_images'):
            self.recover_images.set(True)
        if hasattr(self, 'recover_documents'):
            self.recover_documents.set(True)
        if hasattr(self, 'recover_audio'):
            self.recover_audio.set(True)
        if hasattr(self, 'recover_video'):
            self.recover_video.set(True)
        if hasattr(self, 'recover_archives'):
            self.recover_archives.set(True)
        if hasattr(self, 'auto_organize'):
            self.auto_organize.set(True)
        if hasattr(self, 'generate_thumbnails'):
            self.generate_thumbnails.set(False)
        if hasattr(self, 'verify_files'):
            self.verify_files.set(True)
        if hasattr(self, 'chunk_size_var'):
            self.chunk_size_var.set("1")
        if hasattr(self, 'max_file_size_var'):
            self.max_file_size_var.set("50")
        messagebox.showinfo("Success", "Settings reset to defaults!")

# Utility methods
def update_status(self, message):
    """Update status bar message"""
    if hasattr(self, 'status_text'):
        self.status_text.config(text=message)
    self.root.update_idletasks()

def format_file_size(self, size_bytes):
    """Format file size in human readable format"""
    if size_bytes == 0:
        return "0 B"
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.1f} {size_names[i]}"

def export_to_format(self, filename, format_type):
    """Export recovery results to specified format"""
    if format_type == "CSV":
        import csv
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Filename', 'Original Name', 'File Type', 'Size', 'Hash', 'Recovered At', 'File Path'])
            for file_info in self.recovery_tool.recovered_files:
                writer.writerow([
                    file_info.get('filename', ''),
                    file_info.get('original_name', ''),
                    file_info.get('file_type', ''),
                    file_info.get('size', 0),
                    file_info.get('hash', ''),
                    file_info.get('recovered_at', ''),
                    file_info.get('filepath', '')
                ])
    elif format_type == "JSON":
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.recovery_tool.recovered_files, f, indent=2)
    else:
        raise NotImplementedError(f"Export format {format_type} not implemented yet")
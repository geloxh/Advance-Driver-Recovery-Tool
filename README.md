
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Last%20Update-2025--07--10-brightgreen" alt="Last Update">
</p>

# 🚀 Advanced Driver Recovery Tool

Recover files from corrupted, damaged, or formatted flash drives and storage devices with a modern, user-friendly Python tool.


---

## 📑 Table of Contents

1. [Features](#features)
2. [Screenshots](#screenshots)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [Usage](#usage)
6. [How It Works](#how-it-works)
7. [Output Structure](#output-structure)
8. [Supported File Types](#supported-file-types)
9. [Performance](#performance-considerations)
10. [Troubleshooting](#troubleshooting)
11. [Advanced Usage](#advanced-usage)
12. [Limitations](#limitations)
13. [Legal & Contributing](#legal-and-ethical-considerations)
14. [Support](#support)

---

## ✨ Features

- **Raw Disk Scanning**: Low-level scan for file signatures
- **File Signature Detection**: 20+ file types (JPEG, PNG, PDF, DOC, MP3, ZIP, etc.)
- **Deleted File Recovery**: Recover files after deletion or formatting
- **Progress Tracking**: Real-time progress bar
- **Comprehensive Logging**: Detailed logs for every operation
- **User Interface**: GUI (tabbed) & CLI for advanced users
- **Drive Analysis**: File system health & corruption checks
- **Recovery Reports**: JSON reports of recovered files
- **Multi-platform**: Windows, Linux, macOS
- **Large File Handling**: Efficient, chunked processing
- **File Verification**: MD5 hash for recovered files
- **Batch Processing**: Recover multiple types at once
- **Cancellable**: Stop recovery anytime


---

## 🖼️ Screenshots

<!-- Add screenshots or GIFs here -->
<p align="center">
  <img src="https://via.placeholder.com/600x300?text=GUI+Screenshot" alt="GUI Screenshot" width="60%">
</p>

---

## ⚡ Quick Start

```bash
git clone https://github.com/geloxh/Advance-Driver-Recovery-Tool
cd File-Name
pip install -r requirements.txt
python main.py
```

---

## 🛠️ Installation

**Prerequisites:**
- [Python 3.7+](https://www.python.org/downloads/)
- Administrator/root privileges (for raw disk access)

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Windows users:**
```bash
pip install pywin32
```
More info: [pywin32 on PyPI](https://pypi.org/project/pywin32/)


---

## 🚦 Usage

### GUI Mode (Recommended)

```bash
python main.py
```

**Tabs:**
- File Recovery
- Drive Analysis
- Recovery Log

### Command Line Mode

```bash
python main.py --cli
```

**Steps:**
1. Select drive
2. Choose output directory
3. Monitor progress


---

## 🧠 How It Works

### File Signature Detection
Uses a database of magic numbers to identify file types:

```python
FILE_SIGNATURES = {
    b'\xFF\xD8\xFF': {'ext': '.jpg', 'name': 'JPEG Image'},
    b'\x89\x50\x4E\x47': {'ext': '.png', 'name': 'PNG Image'},
    b'\x25\x50\x44\x46': {'ext': '.pdf', 'name': 'PDF Document'},
    # ... and many more
}
```

### Recovery Process
1. Drive detection
2. Raw scanning (1MB chunks)
3. Signature matching
4. File extraction
5. Verification (checksum)
6. Reporting (JSON)

### File System Analysis
- Detects corruption, permission, and accessibility issues
- Checks free space


---

## 🛡️ Safety Features

- **Read-Only**: Never writes to source drive
- **Safe Recovery**: Output to separate location
- **Original Data Preserved**
- **Robust Error Handling**: Graceful failures, detailed logs, user-friendly messages


---

## 📂 Output Structure

**Recovered Files:**
```
recovered_000001_20231201_143022.jpg
recovered_000002_20231201_143023.pdf
recovered_000003_20231201_143024.mp3
```

**Recovery Report (JSON):**
```json
{
  "recovery_session": {
    "timestamp": "2023-12-01T14:30:22",
    "total_files_recovered": 150,
    "output_directory": "./recovered_files"
  },
  "recovered_files": [...],
  "file_type_summary": {
    "by_type": {
      "JPEG Image": {"count": 45, "total_size": 15728640},
      "PDF Document": {"count": 12, "total_size": 8388608}
    }
  }
}
```


---

## 📑 Supported File Types

| Category     | File Types                | Extensions                  |
|--------------|--------------------------|-----------------------------|
| Images       | JPEG, PNG, GIF, BMP, TIFF| .jpg, .png, .gif, .bmp, .tiff|
| Documents    | PDF, MS Office, RTF      | .pdf, .doc, .rtf            |
| Audio        | MP3, WAV                 | .mp3, .wav                  |
| Video        | MP4                      | .mp4                        |
| Archives     | ZIP, RAR, 7-Zip          | .zip, .rar, .7z             |
| Executables  | Windows PE, Linux ELF    | .exe, .elf                  |


---

## 🚀 Performance Considerations

- **Memory Efficient**: 1MB chunks, configurable
- **Fast**: Multi-threaded scanning (GUI), optimized matching
- **Large Drive Support**: Handles multi-TB drives, file size limits
- **Future**: Resumable operations planned


---

## 🧩 Troubleshooting

**Permission Denied**
- Run as Administrator (Windows) or with sudo (Linux/Mac)
- Ensure drive is not in use

**No Files Recovered**
- Drive may be severely corrupted or physically damaged
- Try other recovery tools

**Slow Performance**
- Large drives take time
- Scan specific partitions
- Use SSD for output

**Error Messages**
- "Cannot access drive": Disconnected, permissions, or hardware failure
- "No file signatures found": Encrypted, severe corruption, or wrong drive


---

## 🧑‍💻 Advanced Usage

### Custom File Signatures
Extend `FILE_SIGNATURES`:
```python
FILE_SIGNATURES[b'\x50\x4B\x03\x04'] = {'ext': '.docx', 'name': 'Word Document'}
```

### Batch Processing
Script for multiple drives (Linux/Mac):
```bash
for drive in /dev/sd*; do
    python main.py --cli --drive $drive --output ./recovery_$drive
done
```

### Integration Example
```python
from main import FlashDriveRecovery
recovery = FlashDriveRecovery()
count = recovery.scan_raw_disk('/dev/sdb1', './output')
report = recovery.generate_recovery_report('./output')
```


---

## ⚠️ Limitations

- Cannot recover overwritten data
- File fragmentation may cause incomplete recovery
- Encrypted files remain encrypted
- Some proprietary formats may not be recognized
- Physical drive damage may prevent access


---

## 📜 Legal and Ethical Considerations

- Only use on drives you own or have explicit permission to access
- Respect privacy and data protection laws
- Do not use for unauthorized data access
- Consider professional data recovery services for critical data


---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add comprehensive tests
4. Submit a pull request

### Adding New File Types
1. Research the file signature (magic number)
2. Add to `FILE_SIGNATURES` dictionary
3. Test with sample files
4. Update documentation


---

## 📝 License

This tool is provided for educational and legitimate data recovery purposes. Users are responsible for compliance with applicable laws and regulations.

---

## 💬 Support

For issues and questions:
1. Check the [troubleshooting](#troubleshooting) section
2. Review the logs for error details
3. Ensure you have the latest version
4. Consider professional data recovery services for critical data

---

**Disclaimer**: This tool is provided as-is without warranty. Always backup important data and use professional data recovery services for critical situations. 
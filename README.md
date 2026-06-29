# 💽 Disk Space Analyzer

A lightweight and fast Python utility that scans directories, analyzes disk usage, identifies the largest files, and summarizes storage consumption by file type.

Built using only Python's standard library—no external dependencies required.

---

## ✨ Features

* 📂 Recursive folder scanning
* 📊 Calculates total disk usage
* 📁 Groups storage by file extension
* 📈 Displays the 10 largest files
* ⚡ Fast and lightweight
* 🛡️ Handles inaccessible files gracefully
* 💻 Cross-platform (Windows, Linux, macOS)

---

## 📸 Preview

```text
======================================================================
                    DISK SPACE ANALYZER
======================================================================

Scanning:
D:\Projects

Total Size : 18.54 GB

Space Used By File Type
----------------------------------------
.mp4            9.82 GB
.zip            4.03 GB
.iso            2.60 GB
.pdf          831.22 MB
.py            42.60 MB

Top 10 Largest Files
----------------------------------------------------------------------
3.40 GB   D:\Projects\Movies\movie1.mp4
2.90 GB   D:\Projects\ISO\ubuntu.iso
1.80 GB   D:\Projects\Backup\data.zip
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/shoykot31/DiskSpaceAnalyzer.git
```

Move into the project directory

```bash
cd DiskSpaceAnalyzer
```

Run the script

```bash
python DiskSpaceAnalyzer.py
```

---

## 🖥 Example

Input

```text
Enter folder path:
D:\Downloads
```

Output

```text
Total Size : 27.6 GB

Largest Files
- movie.mkv
- backup.zip
- ubuntu.iso
```

---

## 📁 Project Structure

```text
DiskSpaceAnalyzer/
│
├── DiskSpaceAnalyzer.py
├── README.md
├── LICENSE
├── requirements.txt
└── screenshots/
```

---

## 🎯 Future Improvements

* Progress bar
* Largest folders
* Interactive delete option
* HTML report
* CSV export
* JSON export
* GUI version
* Pie charts
* Tree map visualization
* Multithreaded scanning

---

## 🤝 Contributing

Contributions, feature requests, and bug reports are welcome.

Feel free to fork the project and submit a pull request.

---

## 📜 License

This project is licensed under the **Beerware License**.

> "As long as you retain this notice you can do whatever you want with this stuff. If we meet someday and you think this stuff is worth it, you can buy me a beer."

---

## 👨‍💻 Author

**Shoykot**

GitHub: https://github.com/shoykot31

If you found this project useful, consider giving it a ⭐.

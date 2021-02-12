#pragma once
#include "pch.h"

class FileHandler
{
private:
	FileHandler();

	static FileHandler s_Instance;

	std::vector<File> m_FileList;
public:
	FileHandler(const FileHandler&) = delete;

	static FileHandler& CreateTransaction();

	void AddFile(std::string FilePath);
	void RemoveFile(std::string FilePath);
};

class File
{
private:
	int Index;
	std::string FilePath;
	FileHandler F_Handler_Instance;

	bool ValidFilePath(const char* FilePath);
public:
	File();

	bool Open(std::string Path);
	bool Close();
	bool Write();

	template<typename T>
	std::vector<T> Read();

	bool Delete();
	bool Exists(std::string Path);
	std::string FileType();
	std::vector<FileStruct> Walk(std::string RootPath);
};

class FileStruct
{
public:
	std::vector <std::string> SubFiles;
	std::vector<FileStruct> SubFolders;
};


#include "Files.h"

// FileHandler defs
FileHandler& FileHandler::CreateTransaction()
{
	return s_Instance;
}

void FileHandler::AddFile(std::string FilePath)
{
	//
}

void FileHandler::RemoveFile(std::string FilePath)
{
	//
}



// File defs
File::File()
{
	//
}

bool File::ValidFilePath(const char* FilePath)
{
	std::fstream File(FilePath);
	if (File.is_open())
	{
		File.close();
		return true;
	}
	File.close();
	return false;
}

bool File::Open(std::string Path)
{
	// Check If Path is Valid
	if (ValidFilePath(Path.c_str()))
	{
		// Add Instance to FilaHandler
		F_Handler_Instance.CreateTransaction().AddFile(Path);

		return true;
	}
	return false;
}

bool File::Close()
{
	// Remove Instance from FileHandler
}

bool File::Write()
{
	//
}

template<typename T>
std::vector<T> File::Read()
{
	//
}

bool File::Delete()
{
	//
}

bool File::Exists(std::string Path)
{
	//
}

std::string File::FileType()
{
	//
}

std::vector<FileStruct> File::Walk(std::string RootPath)
{
	//
}



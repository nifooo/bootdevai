from functions.get_file_content import get_file_content


def test_main():
    print(get_file_content("calculator", "lorem.txt"))
    #print(get_files_info("calculator", "pkg"))
    #print(get_files_info("calculator", "/bin"))
    #print(get_files_info("calculator", "../"))
    

if __name__ == "__main__":
    test_main()
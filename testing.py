if __name__ == '__main__':
    from database.json_file_handle import export_all_to_json_file, import_all_from_json_file
    export_all_to_json_file("./something.json")
    import_all_from_json_file()
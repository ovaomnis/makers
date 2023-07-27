class FileUtils:
    @classmethod
    def get_file_extension(cls, file_name: str):
        import re
        regex = r'\.[^.]+$'
        search = re.findall(regex, file_name)
        if search:
            return search[-1]
        else:
            return ''


print(FileUtils.get_file_extension('document.json'))

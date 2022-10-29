from typing import Dict


class UrlWriter:
    def __init__(self, link_storage: Dict):
        self._link_storage = link_storage

    def write(self):
        raise NotImplemented

    @staticmethod
    def _links_to_print_list(link_storage, result, dept_level=0):
        for key in link_storage.keys():
            result.append("  " * dept_level + key)
            UrlWriter._links_to_print_list(link_storage[key], result, dept_level + 1)

        return result


class ScreenUrlWriter(UrlWriter):
    def write(self):
        print_list = self._links_to_print_list(self._link_storage, [])
        print(*print_list, sep="\n")


class FileUrlWriter(UrlWriter):
    def __init__(self, link_storage, file_path):
        self._file_path = file_path
        super().__init__(link_storage)

    def write(self):
        print_list = self._links_to_print_list(self._link_storage, [])
        with open(self._file_path, "w") as file:
            file.write('\n'.join(print_list))

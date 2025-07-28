import json
import os

__all__ = (
    "utils",
)


class utils:
    def load(path: str, mode: str = "r", encoding: str = "utf8") -> dict:
        """
        load json file

        :param path: json file path
        :param mode: file mode
        :param encoding: file encoding
        :return: dict
        """

        with open(path, mode, encoding=encoding) as jdata:
            return json.load(jdata)

    def save(path: str, data, mode: str = "w", encoding: str = "utf8") -> None:
        """
        save json file

        :param path: json file path
        :param data: data to save
        :param mode: file mode
        :param encoding: file encoding
        :return: None
        """

        with open(path, mode, encoding=encoding) as jdata:
            json.dump(data, jdata, indent=4, ensure_ascii=False)

    def code(message: str, m=None) -> str:
        return f"```{m}\n{message}\n```"

    def get_file_size(path: str) -> str:
        """
        get a file size
        :param path: json file path
        :return: str
        """

        size_in_bytes = os.path.getsize(path)
        size_in_kb = size_in_bytes / 1024
        size_in_mb = size_in_kb / 1024
        size_in_gb = size_in_mb / 1024

        if size_in_gb >= 1:
            return f"{size_in_gb:.2f} GB"
        elif size_in_mb >= 1:
            return f"{size_in_mb:.2f} MB"
        elif size_in_kb >= 1:
            return f"{size_in_kb:.2f} KB"
        else:
            return f"{size_in_bytes} bytes"

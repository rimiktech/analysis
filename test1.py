import json as json_module
from json.decoder import JSONDecodeError
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union
from urllib.parse import parse_qsl
from urllib.parse import urlparse

from requests import PreparedRequest


def _create_key_val_str(input_dict: Union[Dict[Any, Any], Any]) -> str:
    
    def list_to_str(input_list: List[str]) -> str:
        converted_list = []
        for item in sorted(input_list, key=lambda x: str(x)):
            if isinstance(item, dict):
                item = _create_key_val_str(item)
            elif isinstance(item, list):
                item = list_to_str(item)

            converted_list.append(str(item))
        list_str = ", ".join(converted_list)
        return "[" + list_str + "]"

    items_list = []
    for key in sorted(input_dict.keys(), key=lambda x: str(x)):
        val = input_dict[key]
        if isinstance(val, dict):
            val = _create_key_val_str(val)
        elif isinstance(val, list):
            val = list_to_str(input_list=val)

        items_list.append("{}: {}".format(key, val))

    key_val_str = "{{{}}}".format(", ".join(items_list))
    return key_val_str
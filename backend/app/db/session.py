from __future__ import annotations

from collections.abc import MutableMapping


class InMemoryStore(MutableMapping[str, object]):
    def __init__(self):
        self._data: dict[str, object] = {}

    def __getitem__(self, key: str):
        return self._data[key]

    def __setitem__(self, key: str, value):
        self._data[key] = value

    def __delitem__(self, key: str):
        del self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)


store = InMemoryStore()

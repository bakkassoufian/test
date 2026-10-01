"""Numbering for every collection, and resolvers for cross-references.

Cross-references are written by title and resolved here, so a renumbered or
renamed item fails the build instead of leaving a broken reference.
"""

from content import hooks, ideas, prompts, templates


def _number(categories, title_of=lambda item: item[0]):
    index, n = {}, 0
    for _cat in categories:
        for item in _cat[-1]:
            n += 1
            key = title_of(item)
            if key in index:
                raise ValueError(f"Duplicate title: {key}")
            index[key] = n
    return index


PROMPTS = _number(prompts.CATEGORIES)
IDEAS = _number(ideas.CATEGORIES)
HOOKS = _number(hooks.CATEGORIES)
TEMPLATES = {t["name"]: i for i, t in enumerate(templates.TEMPLATES, 1)}

_KINDS = {"prompt": ("Prompt", PROMPTS), "idea": ("Idea", IDEAS), "hook": ("Hook", HOOKS), "template": ("Template", TEMPLATES)}


def ref(kind, title):
    label, index = _KINDS[kind]
    if title not in index:
        raise KeyError(f"Broken reference: {kind} “{title}”")
    n = index[title]
    # Templates and hooks are numbered 01–15 and 01–50 in their files.
    return f"{label} {n:02d}" if kind in ("template", "hook") else f"{label} {n:03d}"


def pref(title):
    return ref("prompt", title)

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


EN_LABELS = {"prompt": "Prompt", "idea": "Idea", "hook": "Hook", "template": "Template"}


def make_ref(prompts_mod, ideas_mod, hooks_mod, templates_mod, labels=EN_LABELS):
    """Return ref(kind, title) for one edition of the kit."""
    indexes = {
        "prompt": _number(prompts_mod.CATEGORIES),
        "idea": _number(ideas_mod.CATEGORIES),
        "hook": _number(hooks_mod.CATEGORIES),
        "template": {t["name"]: i for i, t in enumerate(templates_mod.TEMPLATES, 1)},
    }

    def ref(kind, title):
        index = indexes[kind]
        if title not in index:
            raise KeyError(f"Broken reference: {kind} “{title}”")
        n = index[title]
        # Templates and hooks are numbered 01–15 and 01–50 in their files.
        return f"{labels[kind]} {n:02d}" if kind in ("template", "hook") else f"{labels[kind]} {n:03d}"

    return ref


ref = make_ref(prompts, ideas, hooks, templates)


def pref(title):
    return ref("prompt", title)

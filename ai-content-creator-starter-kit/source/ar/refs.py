"""Cross-reference resolver for the Arabic edition."""

from ar.content import hooks, ideas, prompts, templates
from refs import make_ref

LABELS = {"prompt": "برومبت", "idea": "فكرة", "hook": "خطّاف", "template": "قالب"}

ref = make_ref(prompts, ideas, hooks, templates, LABELS)


def pref(title):
    return ref("prompt", title)

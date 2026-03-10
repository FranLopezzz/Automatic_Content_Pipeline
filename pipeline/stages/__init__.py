from . import brief, portrait, hero, multishot, video, publish

STAGE_MAP = {
    "pending": ("brief", brief.execute),
    "brief": ("portrait", portrait.execute),
    "portrait": ("hero", hero.execute),
    "hero": ("multishot", multishot.execute),
    "multishot": ("video", video.execute),
    "video": ("published", publish.execute),
}

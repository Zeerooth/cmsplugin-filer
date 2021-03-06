from django.conf import settings

VIDEO_WIDTH = getattr(settings, "VIDEO_WIDTH", 320)
VIDEO_HEIGHT = getattr(settings, "VIDEO_HEIGHT", 240)

VIDEO_AUTOPLAY = getattr(settings, "VIDEO_AUTOPLAY", False)
VIDEO_AUTOHIDE = getattr(settings, "VIDEO_AUTOHIDE", False)
VIDEO_LOOP = getattr(settings, "VIDEO_LOOP", False)
VIDEO_CONTROLS = getattr(settings, "VIDEO_CONTROLS", True)
VIDEO_MUTED = getattr(settings, "VIDEO_MUTED", False)
VIDEO_PRELOAD = getattr(settings, "VIDEO_PRELOAD", 'none')
VIDEO_UNITS = getattr(settings, "VIDEO_UNITS", 'px')

VIDEO_BG_COLOR = getattr(settings, "VIDEO_BG_COLOR", "000000")
VIDEO_TEXT_COLOR = getattr(settings, "VIDEO_TEXT_COLOR", "FFFFFF")
VIDEO_SEEKBAR_COLOR = getattr(settings, "VIDEO_SEEKBAR_COLOR", "13ABEC")
VIDEO_SEEKBARBG_COLOR = getattr(settings, "VIDEO_SEEKBARBG_COLOR", "333333")
VIDEO_LOADINGBAR_COLOR = getattr(settings, "VIDEO_LOADINGBAR_COLOR", "828282")
VIDEO_BUTTON_OUT_COLOR = getattr(settings, "VIDEO_BUTTON_OUT_COLOR", "333333")
VIDEO_BUTTON_OVER_COLOR = getattr(settings, "VIDEO_BUTTON_OVER_COLOR", "000000")
VIDEO_BUTTON_HIGHLIGHT_COLOR = getattr(settings, "VIDEO_BUTTON_HIGHLIGHT_COLOR", "FFFFFF")

VIDEO_PLUGIN_ENABLE_ADVANCED_SETTINGS = getattr(settings, "VIDEO_PLUGIN_ENABLE_ADVANCED_SETTINGS", True)

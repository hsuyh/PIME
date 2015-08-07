# -*- coding: utf-8 -*-
from win32con import * # for VK_XXX constants
from ..textService import TextService

class MeowTextService(TextService):
    def __init__(self, client):
        TextService.__init__(self, client)
        self.serviceName = 'DemoText'

    def onActivate(self):
        TextService.onActivate(self)

    def onDeactivate(self):
        TextService.onDeactivate(self)

    def filterKeyDown(self, keyEvent):
        if not self.isComposing():
            if keyEvent.keyCode == VK_RETURN or keyEvent.keyCode == VK_BACK:
                return False
        return True

    def onKeyDown(self, keyEvent):
        candidates = ["喵", "描", "秒", "妙"]
        # handle candidate list
        if self.showCandidates:
            if keyEvent.keyCode == VK_UP or keyEvent.keyCode == VK_ESCAPE:
                self.setShowCandidates(False)
            elif keyEvent.keyCode >= ord('1') and keyEvent.keyCode <= ord('4'):
                i = keyEvent.keyCode - ord('1')
                cand = candidates[i]
                i = self.compositionCursor - 1
                if i < 0:
                    i = 0
                s = self.compositionString[0:i] + cand + self.compositionString[i + 1:]
                self.setCompositionString(s)
                self.setShowCandidates(False)
            return True
        else:
            self.setCandidateList(candidates)
            if keyEvent.keyCode == VK_DOWN:
                self.setShowCandidates(True)
                return True
            pass
        # handle normal keyboard input
        if not self.isComposing():
            if keyEvent.keyCode == VK_RETURN or keyEvent.keyCode == VK_BACK:
                return False
        if keyEvent.keyCode == VK_RETURN or len(self.compositionString) > 10:
            self.setCommitString(self.compositionString)
            self.setCompositionString("")
        elif keyEvent.keyCode == VK_BACK and self.compositionString != "":
            self.setCompositionString(self.compositionString[:-1])
        elif keyEvent.keyCode == VK_LEFT:
            i = self.compositionCursor - 1
            if i >= 0:
                self.setCompositionCursor(i)
        elif keyEvent.keyCode == VK_RIGHT:
            i = self.compositionCursor + 1
            if i <= len(self.compositionString):
                self.setCompositionCursor(i)
        else:
            self.setCompositionString(self.compositionString + "喵")
            self.setCompositionCursor(len(self.compositionString))
        return True

    def filterKeyUp(self, keyEvent):
        return False

    def onKeyUp(self, keyEvent):
        return False

    def onKeyboardStatusChanged(self):
        TextService.onKeyboardStatusChanged(self)

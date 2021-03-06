"""
Copyright (C) 2017 ClaraIO

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Written by ClaraIO <chinodesuuu@gmail.com>, August 2017
"""


from base import Cog, command


class Modules(Cog):
    @command(pass_context=False)
    def load(self, cog: str):
        """ Loads a cog by dotted path """
        self.bot.load_cog(cog)

    @command(pass_context=False)
    def unload(self, cog: str):
        """ Unloads a cog by cog class name """
        self.bot.unload_cog(cog)

    @command(pass_context=False)
    def reload(self, cog: str):
        """ Reloads a cog by cog class name """
        file = self.bot._cogs[cog].__module__
        self.bot.unload_cog(cog)
        self.bot.load_cog(file)


def setup(bot):
    bot.add_cog(Modules(bot))

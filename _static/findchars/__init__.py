from docutils import nodes
from sphinx.util import logging

badChars = ['“','”','—',' ','↩︎︎']
logger = logging.getLogger(__name__)

def checkCodeBlocks(app,doctree):
    for node in doctree.traverse(nodes.literal_block):
        innards = node.astext().splitlines()
        lineNo = 1
        for line in innards:
            for char in badChars:
                if char in line:
                    logger.warning('(' + char + ') found in code block: line ' + str(lineNo), location=node)
            lineNo += 1

def setup(app):
    app.connect('doctree-read',checkCodeBlocks)

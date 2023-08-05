# tei-iiif

## Introduction
TEI-IIIF turns angle brackets into curly brackets. 

To put it in more descriptive terms, it is a Python CLI application that pulls data from [TEI](https://tei-c.org) XML to conformant [IIIF](https://iiif.io) Annotation manifests, as described in the [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/#56-annotation).

TEI-IIIF generates a `.json` manifest for each `<div>` in a given XML file. Within each `<div>` it targets `<p>` elements with a `facs` attribute, which are used as `target` values in the output manifests. It uses `lxml`'s `etree.tostring` method to pull the children of targeted `<p>` elements, saving them as the `value` for that given target. 

## Installation

TK - need to actually work this out.

## Basic use
- TEI-IIIF runs from the command line. TK - need to work this out
- Settings can be found in `settings.yaml`. words to the effect of specifying `base_path`...

## Considerations
- Because TEI-IIIF uses `etree.tostring` to produce the text for annotations, it captures     both tags and text and replicates them. Depending on the input XML, the manifests it outputs may need to be sanitised in order to be used in production, or you may need to sanitise or simplify the XML prior to processing. As use cases can differ dramatically from project to project, TEI-IIIF does not attempt to sanitise output body text.
- However, TEI-IIIF does include regex to sanitise `facs` attributes such that they use `#xywh=` formatting for image selectors. This can be changed according to your use case in `settings.py`
 - By default TEI-IIIF assumes you have XML structured in a format roughly equivalent to the following:

```
<div n="1">
	<p facs=“https://facsimile-server.com/iiif/foo-bar/p1/571,152,1951,1076”>
		<children>...</children>
	</p>
	<p facs="https://facsimile-server.com/iiif/foo-bar/p1/675,728,1949,1320”>
		<children>...</children>
	</p>
</div>
<div n="2">
	<p facs="https://facsimile-server.com/iiif/foo-bar/p2/571,152,1951,1076">
		<children>...</children>
	</p>
	<p facs="https://facsimile-server.com/iiif/foo-bar/p2/675,728,1949,1320">
		<children>...</children>
	</p>
</div>
```
- If your XML differs dramatically from the below then you can change the XPath in `xmlparser.py` and `divjson.py`.
- TEI-IIIF defaults to the [base TEI namespace URI](http://www.tei-c.org/ns/1.0). This can be changed in `settings.yaml`.

## Testing

Um...

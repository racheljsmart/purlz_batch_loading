# purlz_batch_loading
This is a repository for managing purlz batch loading scripts and test data.


## Getting Started

To use this, make sure you have all of this installed and/or running:
- [Vagrant_purlz VM](https://github.com/fsulib/vagrant_purlz)
- Python(install 'requests' library)
- Properly structured XML file to be passed to the RESTful API
- Python script for making HTTP POST requests

**Remember:** Your PURLs' path(ex, "{$insertserver}**_/repository/test/_**") must exist before you begin creating PURLs. You can do this quickly by logging into the PURL Administrator UI if they don't already exist.

## Structuring your XML data

The file 'purl_batch_test1.xml' in this repo, is the xml document I use to run my own tests to create simple PURLs. Resolving a simple PURL will always return an HTTP response code of 302. There are several different types of PURLs that can be created. The data can be modified to another users needs.

To structure your XML document to create multiple 302 PURLs, your document must contain the following syntax:

The "id=" is the PURL you are trying to create. You must include a pre-existing PURL domain (ex, "/repository/test") and the new PURL id (ex, "FSU_test1"). "Type=" indicates the type of PURL you are registering.
`<purl id="/domain/path/<PURL id>" type="302">`

The maintainer is who is responsible for the PURL. They should also have access to the PURL domain.
`<maintainers> <uid>admin</uid> </maintainers>`

To add multiple maintainers, stack the uid child elements.
```
<uid>admin</uid>
<uid>rachel</uid>
```

The target url is the location you would like the PURL to resolve to.
`<target url="https://server.edu/repository/object/namespace:numbersnumbers"/>`


## Sending POST Requests

## Additional resources

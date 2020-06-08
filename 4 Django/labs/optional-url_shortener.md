
# Lab: URL Shortener

## Part 1

A url shortener is a web service that can take long urls (`https://www.google.com/search?source=hp&q=this+is+a+long+url&oq=this+is+a+long+url&gs_l=psy-ab.3..0i22i30k1.1095.3196.0.3437.19.18.0.0.0.0.137.1480.14j4.18.0....0...1.1.64.psy-ab..1.18.1477.0..0j35i39k1j0i131k1j0i67k1j0i20i264k1j33i22i29i30k1.0.aJvctrIr-Ds`) and create a short url (`goo.gl/pEc4vt`). When the short url is accessed, the view will take the specific id associated with that url (`pEc4vt`) and look up the url associated with it in the database. If that URL is found, it then redirects to that URL.

| id | code | url | counter |
| ---|---|---|---|
| `1` | `pEc4vt` | `https://www.google.com/search?s...`| 3 |
| `2` | `fso3Fs` | `https://www..` | 0 |


You *could* use the ID in the url, instead of some code, but that then exposes some details about your database to the public.

Your app should contain the following:
- a model `ShortenedURL` which has the following fields `code` (CharField), `url` (URLField), and `counter` (IntegerField) 
- one view that returns a page for entering in a url to be shortened, and a list of urls that have been shortened (`localhost:8000/shortener/`)
- another view and view for receiving the form submission containing the long url, generating a random string, and saving it to the database (`localhost:8000/shortener/save/`)
- a third view that performs the redirecting, which takes a `code` as a  (`localhost:8000/shortener/pEc4vt/`), you could use [redirect](https://docs.djangoproject.com/en/2.2/topics/http/shortcuts/#redirect) or HttpResponseRedirect. Be sure to include the protocol ("https://") in the urls or redirecting will not work properly.

## Part 2 (optional)

Integrate a user management system with registration, login, and logout functionality. Add a `ForeignKeyField` called `user` to the `ShortenedURL` model. When a url is shortened, it should be saved with the logged-in user. Logged-in users should only see the urls they've shortened.


Flask-Shopify
=============

Flask-Shopify is an extension to *Flask* that adds an interface to the
Python Shopify API (*python-shopify*).

Thanks to Erik Karulf for doing most of the work on ``python-shopify``

Installation
============

Install the extension with one of the following commands:

   $ easy_install Flask-Shopify

or alternatively if you have pip installed:

   $ pip install Flask-Shopify

or get the source from GitHub (http://github.com/lateshowlabs/flask-
shopify).

Note that Flask-Shopify requires ``python-shopify`` as well as
``pyactiveresource``.

   http://github.com/lateshowlabs/python-shopify
   http://github.com/ekarulf/pyactiveresource


Configuration
=============

To get started all you need to do is to instantiate a ``Shopify``
object after configuring the application:

   from flask import Flask
   from flaskext.shopify import Shopify

   app = Flask(__name__)
   app.config.from_object('settings')
   shopify = Shopify(app)

Flask-Shopify requires the following Flask App settings:

+-----------------------------+-----------------------------------------------+
| *SHOPIFY_SHARED_SECRET*     | Your app's shared secret key with Shopify.    |
+-----------------------------+-----------------------------------------------+
| *SHOPIFY_API_KEY*           | Your app's API key.                           |
+-----------------------------+-----------------------------------------------+
| *SHOPIFY_APP_SITE*          | The domain of your Shopify app.               |
+-----------------------------+-----------------------------------------------+

You can get these settings when you create a new app as a Shopify
Partner

If you want to develop your app locally, you can test it by setting
*DEBUG = True*, and by using the following test settings:

+-----------------------------+-----------------------------------------------+
| *SHOPIFY_TEST_SITE*         | Test shop URL.                                |
+-----------------------------+-----------------------------------------------+
| *SHOPIFY_TEST_API_KEY*      | Test shop private app API key.                |
+-----------------------------+-----------------------------------------------+
| *SHOPIFY_TEST_PASSWORD*     | Test shop private app password.               |
+-----------------------------+-----------------------------------------------+

You must define a redirect URL for Shopify to send the user to once
they have installed our app. For example, if you define it as
<SHOPIFY_APP_SITE>/welcome, you can authenticate the shop with the
following example:

   @app.route('/welcome')
   def welcome():
       """Welcome view after a user has installed the app.
       This view authenticates their shop and sets up a session.
       see: http://api.shopify.com/authentication.html
       Expects GET parameters: shop, t, timestamp, signature.
       """

       # if they are logged-in already, redirect them to index
       if request.shopify_session:
           return redirect(url_for('index'))

       # create a session if possible
       try:
           shopify_session = shopify.authenticate(request)
       except Exception, e:
           logging.error('Could not create a session: %s' % str(e))
           flash('Sorry, we couldn\'t log you in.')
           return redirect(url_for('index'))
       else:

           # YOUR CUSTOM LOGIN/INSTALL CODE GOES HERE

           # store the token in the session. It can also be stored in the DB
           session['shopify_token'] = (shopify_session.url, shopify_session.password)
           flash('You are now logged in')
           return redirect(url_for('index'))

You need to provide a *tokengetter* function so that the Shopify
object can create a session. This function must return a token tuple
in the form of (<url>, <password>) for a shop that has the app
installed and has been authenticated.

An example of the *tokengetter* is as follows:

   @shopify.tokengetter
   def get_shopify_token():
       if 'shopify_token' in session:
           return session['shopify_token']
       else:
           return None

There is also a view decorator provided *shopify_login_required* which
requires the Shopify session:

   @shopify_login_required
   @app.route('/preferences')
   def preferences():
       """Show a shop's app preferences only if logged-in."""
       return render_template('preferences.html')

Happy Shopify-ing!

This is a basic example of an app which uses aiohttp. The key code of note is:
1. It runs all the API routes off of the `SCRIPT_PATH` environment variable which is supplied by the custom apps runtime.
This is required because datarobot performs liveness checks to the root path.
2. It routes calls from /<route> to /<route>/. This is important because the liveness checks get sent to the root (eg:
/custom_applications/<id> and we need to redirect that to /custom_applications/<id>/ so the result is not a 404.
3. It runs on port 8080

To get this running on custom apps, simply run `docker build . -t my-aiohttp-custom-app` to build the image, then run
`docker save my-aiohttp-custom-app -o myAiohttpApp.tgz` to save the app to a tgz. That tgz can then be uploaded on the
applications page.


Troubleshooting:
* Some computers (eg M1 Macbooks) require docker images to be built via `docker buildx build --platform linux/amd64 . -t custom-apps-aiohttp`. This requires Docker Desktop, which requires a seperate license.
  

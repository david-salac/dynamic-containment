# Dynamic Containment tender processor
Author: David Salac <https://github.com/david-salac>

This application stores Dynamic Containment tender results from the National
Grid ESO. It fetches results for selected days and organisations and
contains an interface to show them. Technically it is a simple RestFUL
micro-service.

## How to install and use the application?
This section is the simplified user manual.

### Installation guide
1. Install Docker and Docker Compose applications. See some manual:
   * https://docs.docker.com/compose/install/
   * https://docs.docker.com/get-docker/
2. Create an empty folder called `db` in the `infrastructure` folder.
3. Build local stack using the command:
```shell
docker-compose build
```
4. Run local stack using:
```shell
docker-compose up
```
### Software user manual (how to use it)
If your application is up and running, you can start using it. There
are two important end-points:
1. `http://localhost:8000/api/tender/auction-results` - this endpoint
   is a standard GET route, that just shows results stored in the
   database.
2. `http://localhost:8000/api/tender/auction-results/fetch_data/` - this
   is a POST route, that defines parameters for fetching data. Body
   of this end-point is a JSON object with the following structure:
   ```json
   {
      "organization": NAME_OF_ORGANIZATION,
      "datetime_day": DAY_OF_YEAR_WITH_FORMAT_YYYY_MM_DD
   }
   ```
   For example:
   ```json
   {
      "organization": "Habitat Energy Limited",
      "datetime_day": "2021-07-11"
   }
   ```
   this request fetches data for the organization `Habitat Energy Limited`
   for day 11th July 2021.
   
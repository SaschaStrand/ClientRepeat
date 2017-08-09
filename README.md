# ClientRepeat
Copyright &copy; 2017 Sascha Strand

ClientRepeat is a web-based application allows an independent contractor to track his/her clients' re-scheduling and tipping patterns.

For a contractor whose income is based on commission, the over-all rate of re-scheduling among clients can provide valuable data for negotiating a higher rate of commission. And for anyone who maintains long-term client relationships that include regular gratuity, data on this aspect of compensation can allow a contractor to prioritize scheduling and services to their most valuable clients.

## How To Use

Note: ClientRepeat includes only the most minimal security features (effectively none), so in cases where client confidentiality is important, please run it only locally.

1.  Create a username and password and log in

1.  In the Clients tab input a list of your clients and the identifying data about them that is important to you in this application.

1.  Use the form in the New Appointments tab to track each appointment completed.

1.  Use the Reports tab to find a sorted list of clients by average total gratuity as well as the average rate of re-scheduling among all clients and a sorted list of clients by rate of re-scheduling.

## Status

The front-end is complete. I am currently implementing the back end as we learn about databases in my web development class.

## To Do

For single-user version of application:
* Add analytics: sorted list of clients by average tip
* Add analytics: average rate of re-scheduling
* Add analytics: sorted list of clients by rate of re-scheduling
* Add pre-population of client name in new appt input
* Remove debugging print statements

For demonstration
* Create some user data

## Done
* Add check for foreign key validation in input
* Be able to create an appointment associated with a client
* Be able to log a new user
* Correct error message from adding an appointment for a client who doesn't exist
* Create border requiring login around content
* Be able to log a user in
* Be able to log a user out
* Modify database to distinguish different users

## Limitations

* Client information must be entered manually
* Reporting data is available only through the front-end
* Reporting data is available only in tabular form (Tufte would be sad)
* Almost no input-validation in forms
* There is no way to edit a client's information.
* Clients must have unique names (even across users)

## License

This work is made available under the MIT license.

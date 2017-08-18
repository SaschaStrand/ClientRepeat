# ClientRepeat
Copyright &copy; 2017 Sascha Strand
Available open source through the MIT License

ClientRepeat is a web-based application allows an independent contractor to track his/her clients' re-scheduling and tipping patterns.

For a contractor whose income is based on commission, the over-all rate of re-scheduling among clients can provide valuable data for negotiating a higher rate of commission. And for anyone who maintains long-term client relationships that include regular gratuity, data on this aspect of compensation can allow a contractor to prioritize scheduling and services to their most valuable clients.

## Video Demonstration

Video demonstrations of ClientRepeat can be found here:

[New user](https://youtu.be/i9pQlqs8Shc)

[User with established clients](https://youtu.be/yYw9iGMiHXo)

As well as in their [raw video formats](https://drive.google.com/drive/folders/0B-S6GlZ4FikrTzRkV2wwTXBkbDA?usp=sharing)

## How To Use

Note: ClientRepeat includes only the most minimal security features (effectively none), so in cases where client confidentiality is important, please run it only locally.

1.  Create a username and password and log in

1.  In the Clients tab input a list of your clients and the identifying data about them that is important to you in this application.

1.  Use the form in the New Appointments tab to track each appointment completed.

1.  Use the Reports tab to find a sorted list of clients by average total gratuity as well as the average rate of re-scheduling among all clients and a sorted list of clients by rate of re-scheduling.

## How to build

This project can be built in two main steps.

The first is simply to clone the main branch of the distribution or download the sourcecode of the most recent release. 

The second step is to build a MySQL database based on the schema.txt file and connected to the application in the app.py script under the heading "Configure Database". 

From there, the program runs well locally. It is not yet deployed publicly as a web service.

## Status

The front and back-end are complete. Under manual testing, the application works well with the exception of the limitations listed below.

## Limitations

* Client information must be entered manually
* Reporting data is available only through the front-end
* Reporting data is available only in tabular form (Tufte would be sad)
* Almost no input-validation in forms
* There is no way to edit a client's information.
* Clients must have unique names (even across users)

## License

This work is made available under the MIT license.

## Contact Info

This project is maintained by myself, Sascha Strand.
I can be reached at sastrand at pdx dot edu.
And please feel free to report any bugs through this github page. 

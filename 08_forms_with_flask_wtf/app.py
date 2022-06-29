"""
Date of Birth Form
At this point, you have become familiar with defining, rendering,
and adapting your view functions to forms and fields. To practice making more forms,
you will create a new route that displays a form asking for date of birth.
Upon submitting the form, you will flash a message to display their Zodiac sign
(Libra, Cancer, etc) or Chinese Zodiac animal (Rat, Ox, etc).

Guidelines
DateField
To accomplish this, you will use a wtforms.fields.DateField field in your form.
This field is just like StringField in that it accepts a label.
 You will need to make sure your user can't submit the form without putting in a date.

View Function
As you learned, you'll need a view function to create your form instance.
 Call your view function zodiac and make it a handler for the route '/zodiac'.
  Whenever the form is successfully validated, redirect the browser to the index page '/'.

Template
Make a new template called zodiac.html and make it inherit from the base template base.html.
 Render your new form here. You shouldn't need anything else except the form, but feel free to be creative!

Flash a Message
Once the user submits the form, have the webapp flash a message that displays what their Zodiac sign or
Chinese Zodiac animal is. This will involve working with some datetime.dates,
 but it should be a simple calculation otherwise.
  If you have trouble with the datetime library and need help,
   you can ask a question on our forum or ask your mentor for help.

Have Fun!
Most of all, have fun with it! People learn best when they have fun with whatever
 it is they are doing, so don't be afraid to deviate from these guidelines.

Don't spend too much time on it though, because you'll be diving into
 databases in the next section. Forms tie into databases because they
  can keep track of what data users give via forms!"""
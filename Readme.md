Flask Blog Application

A simple Flask web application that displays blog posts, an about page, and a contact form. It fetches posts from an external API and allows users to contact via a form that sends emails.
Features

    Home Page (/): Displays a list of blog posts fetched from an external API.
    About Page (/about): Displays information about the application.
    Post Page (/post/<int:index>): Shows details of a specific blog post based on the post ID.
    Contact Page (/contact): Allows users to send a message. Submissions trigger an email to be sent.

Usage

    Home Page: Visit http://127.0.0.1:5000/ to see the list of blog posts.
    About Page: Visit http://127.0.0.1:5000/about to read about the application.
    Post Page: Visit http://127.0.0.1:5000/post/<id> to view a specific post.
    Contact Page: Visit http://127.0.0.1:5000/contact to send a message.

Email Configuration

The contact form sends an email using the SMTP server provided by Gmail. Ensure you have set up your email credentials correctly in the environment variables. If using Gmail with two-factor authentication (2FA), you may need to generate an App Password and use that instead of your regular password.
Security Notes

    Environment Variables: Do not hardcode sensitive information like passwords in your code. Use environment variables instead.
    Email Configuration: Ensure your email account settings allow SMTP access and be cautious with your credentials.

License

This project is licensed under the MIT License - see the LICENSE file for details.
/* Class-based Components can't use React Hooks */
/* Die Homepage Seite ist die Hauptseite dieser Applikation */

import * as React from 'react';


class Homepage extends React.Component {
    constructor(props) {
        super(props);
        this. state = {};
    }

    render() {
        const { user } = this.props;
        return (
            <Grid style={{ display: "flex", justifyContent: "center" }}>
                <Container >
                    <br></br>
                    <div>
                        <h3> Hallo {user.displayName} 🤓 </h3>
                        <h1> Willkommen auf meiner Übungsseite! </h1>
                        <h3> Hier möchte ich eine Seite erstellen, auf welcher meine Freune einen Freundebucheintrag erstellen können. </h3>
                    </div>

                </Container>
            </Grid>
        );
    }
}

/** PropTypes */
Homepage.propTypes = {
    /** The user to be rendered */
    user: PropTypes.object,

}

export default Homepage;



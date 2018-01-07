import { render } from 'preact';
import { Route, Link } from 'react-router-dom';
import { MemoryRouter } from 'react-router';

const Home = () => (
	<div>
		<h2>Home</h2>
	</div>
);

const About = () => (
	<div>
		<h2>About</h2>
	</div>
);

const Default = () => (<h3>Please select a topic.</h3>);

const Topics = ({ match }) => (
	<div>
		<h2>Topics</h2>
		<ul>
			<li><Link to={`${match.url}/rendering`}>Rendering with React</Link></li>
			<li><Link to={`${match.url}/components`}>Components</Link></li>
			<li><Link to={`${match.url}/props-v-state`}>Props v. State</Link></li>
		</ul>

		<Route path={`${match.url}/:topicId`} component={Topic} />
		<Route exact path={match.url} component={Default} />
	</div>
);

const Topic = ({ match }) => (
	<div>
		<h3>{match.params.topicId}</h3>
	</div>
);

const App = () => (
	<MemoryRouter>
		<div>
			<ul>
				<li><Link to="/">Home</Link></li>
				<li><Link to="/about">About</Link></li>
				<li><Link to="/topics">Topics</Link></li>
			</ul>

			<hr />
			<Route exact path="/" component={Home} />
			<Route path="/about" component={About} />
			<Route path="/topics" component={Topics} />
		</div>
	</MemoryRouter>
);

render(<App />, document.body);

import './App.css';
import { Band } from './Band.js';

function App() {
  let bandName = "Battle Beast";
  return (
    <div className="App">
      <h1>Bands I am seeing Friday</h1>
      <ul>
        <Band name={bandName} />
        <Band name="The Amity Affliction" />
        <Band name="Imagine Dragons" />
        <Band name="Weezer" />
        <Band name="Three Doors Grace" />
      </ul>
      <button onClick={() => { bandName = "Toto" }}>Click me!</button>
    </div>
  );
}

export default App;

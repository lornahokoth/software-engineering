import { fireEvent, render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

test('input text shows up when button is pressed' , () => {
  render(<App/>);
  const buttonElement = screen.getByText("Click me!")
  const inputElement = screen.getByTestId("input-field");
  
  fireEvent.change(
    inputElement, {target: {value: "My Chemical Romance"}}
  );
  fireEvent.click(buttonElement);
  
  const newTextElement = screen.getByText("My Chemical Romance");
  expect(newTextElement).toBeInTheDocument();
});

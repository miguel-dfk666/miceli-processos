import React from 'react';

interface DropdownProps {
  options: string[];
  selectedOption: string;
  onSelect: (option: string) => void;
}

const Dropdown: React.FC<DropdownProps> = ({ options, selectedOption, onSelect }) => {
  return (
    <select
      value={selectedOption}
      onChange={(e) => onSelect(e.target.value)}
      className="bg-gray-100 border border-gray-400 p-2 rounded w-64"
    >
      {options.map((option) => (
        <option key={option} value={option}>
          {option}
        </option>
      ))}
    </select>
  );
};

export default Dropdown;

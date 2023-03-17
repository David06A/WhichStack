type ThemeToggleButtonProps = {
  isLightMode: boolean;
  setIsLightMode: ( isLightMode: boolean ) => void;
};

export const ThemeToggleButton = ( {
  isLightMode,
  setIsLightMode,
}: ThemeToggleButtonProps ) =>
{
  return (
    <label className="toggle">
      <input
        type="checkbox"
        checked={ isLightMode }
        onChange={ () => setIsLightMode( !isLightMode ) }
      />
      <span className="slider"></span>
    </label>
  );
};

import { CalculateMetadataFunction, Composition } from "remotion";
import { R02Video } from "./R02Video";

type Props = {};

const calculateMetadata: CalculateMetadataFunction<Props> = () => {
  return {};
};

export const MyComposition = () => {
  return (
    <Composition
      id="R02"
      component={R02Video}
      durationInFrames={1800}
      fps={30}
      width={1920}
      height={1080}
      calculateMetadata={calculateMetadata}
    />
  );
};
